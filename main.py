import requests
import json
import random

# API anahtarınızı buraya ekleyin
API_KEY = "YOUR_API_KEY"

def get_weather_info(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        weather_description = weather['description']
        return f"{location.capitalize()} için hava durumu:\nSıcaklık: {temperature}°C\nDurum: {weather_description}"
    else:
        return "Hava durumu bilgisi alınamadı. Lütfen doğru bir şehir adı girin."

def get_cultural_info(query):
    info = {
        "farklı kültürler": "Farklı kültürler hakkında bilgiler:\n1. Japon kültürü: Geleneksel çay seremonisi, samuraylar, ve manga.\n2. İtalyan kültürü: Rönesans sanatı, pizza, ve şarap.\n3. Meksika kültürü: Taco, Mariachi müziği, ve Mayalar."
    }
    return info.get(query, "Kültürel bilgi hakkında daha fazla bilgi almak ister misiniz?")

def get_science_and_technology_info():
    return "Bilim ve teknoloji hakkında bazı bilgiler:\n1. Yapay zeka, veri analizi ve otomasyon alanında büyük ilerlemeler kaydedilmektedir.\n2. Kuantum bilgisayarlar, geleneksel bilgisayarlara göre çok daha hızlı hesaplama yapabilir.\n3. Uzay keşifleri ve Mars'a insan göndermek için çalışmalar devam ediyor."

def get_daily_tips():
    return "Günlük yaşam ve verimlilik için bazı tavsiyeler:\n1. Her gün yeterli su içmeye özen gösterin.\n2. Düzenli egzersiz yapın ve sağlıklı beslenin.\n3. Hedeflerinizi belirleyin ve planlı bir şekilde ilerleyin.\n4. İş ve kişisel yaşam arasında denge kurmaya çalışın."

def get_game_news():
    return "Güncel oyun haberleri için popüler oyun sitelerini ziyaret etmenizi öneririm."

def get_history_info(year):
    history = {
        "1453": "1453'te Konstantinopolis'in fethi, Bizans İmparatorluğu'nun sona erdiği yılı işaret eder.",
        "1923": "1923, Türkiye Cumhuriyeti'nin kurulduğu yıl olarak bilinir.",
        "1969": "1969'da Apollo 11 Ay'a iniş yaptı ve Neil Armstrong ilk adımını attı."
    }
    return history.get(year, "Bu yıl hakkında bilgi bulunmamaktadır.")

def solve_math_problem(problem):
    try:
        return f"Sonuç: {eval(problem)}"
    except Exception:
        return "Matematiksel ifade geçersiz."

def get_personal_recommendations():
    return "Film, müzik, kitap önerileri için ilgi alanlarınızı belirtirseniz daha kişiselleştirilmiş öneriler sunabilirim."

def get_motivational_quote():
    quotes = [
        "Başarı, küçük çabaların tekrarıdır.",
        "Hayatta en büyük mutluluk, başkalarının başarılarına katkıda bulunmaktır.",
        "Geleceği tahmin etmenin en iyi yolu, onu yaratmaktır."
    ]
    return random.choice(quotes)

def get_success_story():
    stories = [
        "Steve Jobs, genç yaşta Apple'ı kurarak teknoloji dünyasında devrim yaptı.",
        "Marie Curie, radyoaktivite üzerine yaptığı çalışmalarla Nobel Ödülü kazandı ve bilime büyük katkı sağladı.",
        "Elon Musk, SpaceX ve Tesla ile inovasyonun öncüsü oldu."
    ]
    return random.choice(stories)

def get_fitness_tips():
    return "Egzersiz ve sağlıklı yaşam için bazı tavsiyeler:\n1. Haftada en az 150 dakika orta düzeyde aerobik egzersiz yapın.\n2. Kas güçlendirici egzersizler haftada iki gün yapılmalıdır.\n3. Düzenli olarak su için ve dengeli beslenin."

def get_healthy_recipes():
    return "Sağlıklı tarifler:\n1. Quinoa salatası: Quinoa, taze sebzeler ve limonlu sos.\n2. Izgara tavuk: Baharatlı ızgara tavuk göğsü, yanında sebzeler.\n3. Smoothie: Yoğurt, meyve ve biraz bal ile yapılan sağlıklı smoothie."

def get_hobby_recommendations():
    return "Yeni hobiler:\n1. Bahçecilik: Bitkiler yetiştirerek doğa ile vakit geçirin.\n2. Resim Yapma: Yaratıcılığınızı ifade edin.\n3. Fotoğrafçılık: Çevrenizdeki güzellikleri yakalayın."

def get_book_recommendations():
    return "Kitap önerileri:\n1. '1984' - George Orwell\n2. 'Savaş ve Barış' - Lev Tolstoy\n3. 'Yüzüklerin Efendisi' - J.R.R. Tolkien"

def translate_text(text, target_language):
    # Placeholder for translation functionality
    return f"{text} metni {target_language} diline çevrildi."

def get_language_learning_tips():
    return "Dil öğrenme tavsiyeleri:\n1. Günlük olarak pratik yapın.\n2. Dil öğrenme uygulamaları kullanın.\n3. O dili konuşulan ortamlarda bulunmaya çalışın."

def get_financial_advice():
    return "Finansal tavsiyeler:\n1. Tasarruf yapmayı alışkanlık haline getirin.\n2. Yatırım yaparken riskleri değerlendirin.\n3. Bütçenizi planlayın ve takip edin."

def get_budgeting_tips():
    return "Bütçe yönetimi ipuçları:\n1. Gelir ve giderlerinizi takip edin.\n2. Tasarruf hedefleri belirleyin.\n3. Gereksiz harcamaları azaltın."

def get_personal_growth_tips():
    return "Kişisel gelişim tavsiyeleri:\n1. Kişisel hedefler belirleyin ve onlara ulaşmak için plan yapın.\n2. Kendinizi geliştirmek için yeni beceriler öğrenin.\n3. Düzenli olarak kişisel değerlendirme yapın."

def get_time_management_tips():
    return "Zaman yönetimi ipuçları:\n1. Önceliklerinizi belirleyin ve görevleri sıralayın.\n2. Zaman blokları oluşturun ve bunlara sadık kalın.\n3. Procrastinasyonu önlemek için hedefler koyun."

def get_movie_recommendations():
    return "Film önerileri:\n1. 'The Shawshank Redemption' (Esaretin Bedeli)\n2. 'Inception' (Başlangıç)\n3. 'The Godfather' (Baba)\n4. 'The Dark Knight' (Kara Şövalye)\n5. 'Pulp Fiction' (Ucuz Roman)\n6. 'Forrest Gump'\n7. 'Fight Club' (Dövüş Kulübü)\n8. 'The Matrix' (Matrix)\n9. 'Interstellar' (Yıldızlararası)\n10. 'Parasite' (Parazit)"

def list_features():
    features = """
    Mevcut Özellikler:
    1. Hava durumu bilgisi
    2. Kültürel bilgiler
    3. Bilim ve teknoloji hakkında bilgiler
    4. Günlük tavsiyeler
    5. Oyun haberleri
    6. Tarih bilgisi
    7. Matematiksel problemler çözme
    8. Kişisel öneriler
    9. Motivasyonel alıntılar
    10. Başarı hikayeleri
    11. Egzersiz tavsiyeleri
    12. Sağlıklı tarifler
    13. Yeni hobiler önerileri
    14. Kitap önerileri
    15. Çeviri hizmeti
    16. Dil öğrenme tavsiyeleri
    17. Finansal tavsiyeler
    18. Bütçe yönetimi ipuçları
    19. Kişisel gelişim tavsiyeleri
    20. Zaman yönetimi ipuçları
    21. Film önerileri
    """
    return features

def get_response(user_input):
    user_input = user_input.lower()
    
    if "merhaba" in user_input:
        return "Merhaba!"
    elif "nasılsın" in user_input:
        return "İyiyim, teşekkür ederim. Siz nasılsınız?"
    elif "naber" in user_input:
        return "İyiyim, siz nasılsınız?"
    elif "öneri" in user_input:
        return get_personal_recommendations()
    elif "hava durumu" in user_input:
        location = user_input.split("hava durumu")[1].strip()
        return get_weather_info(location)
    elif "kültürel" in user_input:
        return get_cultural_info(user_input)
    elif "bilim" in user_input or "teknoloji" in user_input:
        return get_science_and_technology_info()
    elif "tavsiye" in user_input:
        return get_daily_tips()
    elif "oyun" in user_input:
        return get_game_news()
    elif "tarih" in user_input:
        year = user_input.split("tarih")[1].strip()
        return get_history_info(year)
    elif "matematik" in user_input:
        problem = user_input.split("matematik")[1].strip()
        return solve_math_problem(problem)
    elif "motivasyon" in user_input:
        return get_motivational_quote()
    elif "başarı" in user_input:
        return get_success_story()
    elif "egzersiz" in user_input:
        return get_fitness_tips()
    elif "sağlıklı tarifler" in user_input:
        return get_healthy_recipes()
    elif "hobiler" in user_input:
        return get_hobby_recommendations()
    elif "kitap" in user_input:
        return get_book_recommendations()
    elif "çeviri" in user_input:
        text = user_input.split("çeviri")[1].strip()
        return translate_text(text, "Türkçe")
    elif "dil öğrenme" in user_input:
        return get_language_learning_tips()
    elif "finans" in user_input:
        return get_financial_advice()
    elif "bütçe" in user_input:
        return get_budgeting_tips()
    elif "kişisel gelişim" in user_input:
        return get_personal_growth_tips()
    elif "zaman yönetimi" in user_input:
        return get_time_management_tips()
    elif "film" in user_input:
        return get_movie_recommendations()
    elif "özellikler" in user_input:
        return list_features()
    else:
        return "Bu konuda size nasıl yardımcı olabilirim?"

def main():
    print("Merhaba! Size nasıl yardımcı olabilirim? (Çıkmak için 'çıkış' yazın)")
    
    while True:
        user_input = input("Soru: ").strip()
        if user_input.lower() == "çıkış":
            print("Hoşça kal! Gününüz güzel geçsin.")
            break
        
        response = get_response(user_input)
        print("Yanıt:", response)

if __name__ == "__main__":
    main()
