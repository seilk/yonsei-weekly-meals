# Yonsei Weekly Meals Aggregator

연세대학교 + 세브란스(아라마크) 주간 식단을 모아서 `README`와 `data/weekly.json`을 자동 생성합니다.

<details>
<summary>메타 정보 (Last updated / Sources)</summary>

- Last updated (KST): **2026-09-16T12:58:57+09:00**
- Sources:
  - Yonsei weekly menu: https://www.yonsei.ac.kr/_custom/yonsei/m/menu.jsp
  - Aramark mobile: http://m.yonsei.aramark.co.kr/mobile/yonsei/index.jsp

</details>

## 수집 경고

- Aramark parser failed: HTTPConnectionPool(host='m.yonsei.aramark.co.kr', port=80): Max retries exceeded with url: /mobile/yonsei/index.jsp?meal\_time=m&fz\_no=1 (Caused by NameResolutionError("HTTPConnection(host='m.yonsei.aramark.co.kr', port=80): Failed to resolve 'm.yonsei.aramark.co.kr' (\[Errno -3\] Temporary failure in name resolution)"))
- Aramark data is empty.
- Aramark expected restaurant missing: 종합관
- Aramark expected restaurant missing: 제중관

## 식당별 운영시간

### 연세대학교 맛나샘
- **학기중**
  - 평일
    - 맛나샘 08:00\~18:30
    - (쉬는시간 14:00\~16:00)
    - 아침 : 08:00\~09:30
    - 점심 : 11:00\~14:00
    - 저녁 : 16:00\~18:30
    - 스낵 10:00\~18:30
    - (쉬는시간 14:00\~15:00)
  - 주말
    - 맛나샘 (점심식사) 11:00\~14:00
    - 스낵(마이보글) 09:00\~14:00
- **방학중**
  - 평일
    - 점심 : 11:00\~14:00
    - 저녁 : 16:00\~18:00
    - 스낵 : 09:00\~18:00
  - 주말
    - 스낵 : 09:00\~14:00
    - 식사 : 11:00\~14:00

### 연세대학교 한경관(어울샘)
- **학기중**
  - 1층 운영시간: 10:40\~14:00
  - 2층 중식 운영시간: 10:40\~13:50
  - 2층 석식 운영시간: 16:30\~18:50
- **방학중**
  - 1층 운영시간: 10:40\~14:00
  - 2층 중식 운영시간: 10:40\~13:50
  - 2층 석식 운영시간: 16:30\~18:20
- 주말
  - 주말 및 공휴일은 휴무이며,
  - 각 매장 상황에 따라 운영시간은 변경될 수 있음.

### 세브란스 종합관
-

### 세브란스 제중관
-

## 오늘 메뉴

**오늘:** 수(09/16)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | 🌄 **아침 (조식)**: 해물짬뽕탕 Spicy Seafood Soup (1,000원), 쌀밥, 미트볼카레라이스 Meatball Curry Rice (1,000원), 우동국<br>🌄 **조식자율바**: 청포묵김가루무침, 간장궁채절임, 배추김치<br>**탕맛기픈**: 부대찌개 Budae Jjigae (Korean Army Stew) (5,500원), 닭매운찜 Spicy Braised Chicken (6,000원)<br>**동방식객 /모던키친**: 새우튀김우동& 핫도그\*케찹 Udon with Fried Shrimp & Hot Dog (6,500원), 치킨난반 Chicken Nanban (5,700원)<br>**공통메뉴**: 쌀밥, 그린샐러드&오리엔탈D<br>**샐러드바**: 오복지, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (5,700원), 해장라면 Bean Sprout& Dried Pollack Ramen (5,700원), 자파게티 Noodles with Black Soybean Sauce (5,700원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (5,700원), 폭탄주먹밥(햄) Rice Ball (Ham) (5,700원), 폭탄주먹밥(참치) Rice Ball (Tuna) (5,700원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (5,700원), 즉석철판떡볶이 Stir-fried Rice Cake (5,700원), 닭강정 Sweet and Sour Chicken (5,700원), 공기밥 Rice (5,700원), 치즈사리 Add ( Cheese) (5,700원), 떡사리 Add ( Rice cake) (5,700원), 날계란사리 Add ( Raw Egg ) (5,700원) |
| 연세대학교 한경관(어울샘) | ☀️ **1층 중식**: 감자탕, 동그랑땡전, 야채묵무침, 오이지무침, 콩자반, 계란후라이, 김치, 숭늉 Gamjatang (Pork Bone Stew), Donggeurangttaeng (Korean Meat Pancakes), Seasoned Jelly and Vegetables, Seasoned Pickled Cucumber, Sweet Braised Black Soybeans, Fried Egg, Kimchi, Sungnyung (Traditional Scorched Rice Tea (7,900원)<br>☀️ **2층 중식**: 국, 게살스프, 대패삼겹두부조림, 아마트리치아나파스타, 제육불고기, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Crab Meat Soup, Braised Tofu with Thinly Sliced Pork Belly, Amatriciana Pasta, Stir-fried Spicy Pork Bulgogi, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원)<br>🌛 **2층 석식**: 국, 게살스프, 곱창부대볶음, 탄탄파스타, 제육불고기, 햄버섯야채솥밥, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Crab Meat Soup, Stir-fried Beef Intestines and Budae-jjigae Ingredients, Dan Dan Pasta, Stir-fried Spicy Pork Bulgogi, Mushroom and Ham Vegetable Stone Pot Rice, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원) |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

## 요일별 보기

### 요일 빠른 이동
[월(09/14)](#day-mon) | [화(09/15)](#day-tue) | [수(09/16)](#day-wed) | [목(09/17)](#day-thu) | [금(09/18)](#day-fri) | [토(09/19)](#day-sat) | [일(09/20)](#day-sun)

<a id="day-mon"></a>
### 월(09/14)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | 🌄 **아침 (조식)**: 콩나물해장국 Bean Sprout Hangover Soup (1,000원), 쌀밥, 닭갈비덮밥 Spicy Stir‑Fried Chicken over Rice (1,000원), 우동국<br>🌄 **조식자율바**: 알감자조림, 미역초무침, 배추김치<br>**탕맛기픈**: 차돌된장찌개 Beef Brisket Soybean Paste Stew (6,300원), 돌솥날치알밥 Hot Stone Pot Flying Fish Roe Rice (5,500원)<br>**동방식객 /모던키친**: 모듬가스정식 (치즈돈가스 & 생선커틀렛) Assorted Cutlet Set <br>(Cheese Tonkatsu & Fish Cutlet) (6,900원), 돈육생채소비빔밥 Pork and Fresh Vegetable Bibimbap (5,800원)<br>**공통메뉴**: 쌀밥, 푸실리샐러드<br>**샐러드바**: 마늘종지무침, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (5,800원), 해장라면 Bean Sprout& Dried Pollack Ramen (5,800원), 자파게티 Noodles with Black Soybean Sauce (5,800원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (5,800원), 폭탄주먹밥(햄) Rice Ball (Ham) (5,800원), 폭탄주먹밥(참치) Rice Ball (Tuna) (5,800원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (5,800원), 즉석철판떡볶이 Stir-fried Rice Cake (5,800원), 닭강정 Sweet and Sour Chicken (5,800원), 공기밥 Rice (5,800원), 치즈사리 Add ( Cheese) (5,800원), 떡사리 Add ( Rice cake) (5,800원), 날계란사리 Add ( Raw Egg ) (5,800원) |
| 연세대학교 한경관(어울샘) | ☀️ **1층 중식**: 김치콩나물국, 소고기버섯카레, 대패삼겹두부조림, 돈가스, 어묵우엉채볶음, 콩자반, 계란후라이, 김치, 숭늉 Kimchi & Bean Sprout Soup, Beef and Mushroom Curry, Braised Tofu with Thinly Sliced Pork Belly, Pork Cutlet, Stir-fried Fish Cake and Shredded Burdock Root, Sweet Braised Black Soybeans, Fried Egg, Kimchi, Sungnyung (Traditional Scorched Rice Tea) (7,900원)<br>☀️ **2층 중식**: 국, 하이라이스덮밥, 소세지어묵야채볶음, 탄탄파스타, 제육불고기, 햄버섯야채솥밥, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, High-Rice Bowl (Japanese-style Curry Rice Bowl), Stir-fried Sausage, Fish Cake, and Vegetables, Dan Dan Pasta, Stir-fried Spicy Pork Bulgogi, Mushroom and Ham Vegetable Stone Pot Rice, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원)<br>🌛 **2층 석식**: 국, 하이라이스덮밥, 대패삼겹두부조림, 제육고추장크림파스타, 제육불고기, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, High-Rice Bowl (Japanese-style Curry Rice Bowl), Braised Tofu with Thinly Sliced Pork Belly, Spicy Pork Gochujang Cream Pasta, Stir-fried Spicy Pork Bulgogi, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원) |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

<a id="day-tue"></a>
### 화(09/15)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | 🌄 **아침 (조식)**: 사골옹심이떡만둣국 Beef Bone Soup with Ongshimi Tteok & Dumplings (1,000원), 쌀밥, 소시지두부폭찹덮밥 Sausage & Tofu Cutlet Rice Bowl (1,000원), 우동국<br>🌄 **조식자율바**: 계란찜, 그린샐러드&오리엔탈D, 배추김치<br>**탕맛기픈**: 쇠고기뭇국&당면사리 Beef and Radish Soup with Glass Noodles (5,000원), 돼지고기김치찌개 Pork and Kimchi Stew (5,200원)<br>**동방식객 /모던키친**: \[동방식객\]\_하이디라오 마라훠궈 Haidilao Mala Hot Pot (7,800원), 등심돈가스정식 (밥,양상추샐러드포함) Pork Loin Cutlet Set (6,200원)<br>**공통메뉴**: 쌀밥, 콩나물무침<br>**샐러드바**: 간장고추지, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (6,200원), 해장라면 Bean Sprout& Dried Pollack Ramen (6,200원), 자파게티 Noodles with Black Soybean Sauce (6,200원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (6,200원), 폭탄주먹밥(햄) Rice Ball (Ham) (6,200원), 폭탄주먹밥(참치) Rice Ball (Tuna) (6,200원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (6,200원), 즉석철판떡볶이 Stir-fried Rice Cake (6,200원), 닭강정 Sweet and Sour Chicken (6,200원), 공기밥 Rice (6,200원), 치즈사리 Add ( Cheese) (6,200원), 떡사리 Add ( Rice cake) (6,200원), 날계란사리 Add ( Raw Egg ) (6,200원) |
| 연세대학교 한경관(어울샘) | ☀️ **1층 중식**: 두부무된장국, 곤드레솥밥, 바싹제육볶음, 비빔국수, 콩나물무침, 멸치볶음, 계란후라이, 김치, 숭늉 Doofu-Moe-Doenjang-guk (Tofu and Radish Soybean Paste Soup), Gondre-sotbap (Gondre Herb Rice in a Stone Pot), Crispy Stir-fried Pork, Bibim-guksu (Spicy Mixed Noodles), Seasoned Bean Sprouts, Stir-fried Anchovies, Fried Egg, Kimchi, Sungnyung (Traditional Scorched Rice Tea) (7,900원)<br>☀️ **2층 중식**: 국, 마파두부덮밥, 모듬튀김, 제육고추장크림파스타, 제육불고기, 햄버섯야채솥밥, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Mapo Tofu Rice Bowl, Assorted Tempura/Fried Fritters, Spicy Pork Gochujang Cream Pasta, Stir-fried Spicy Pork Bulgogi, Mushroom and Ham Vegetable Stone Pot Rice, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원)<br>🌛 **2층 석식**: 국, 마파두부덮밥, 닭다리살김치볶음, 얼큰볶음대파라면, 제육불고기, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Mapo Tofu Rice Bowl, Stir-fried Chicken Thigh with Kimchi, Spicy Stir-fried Green Onion Ramen, Stir-fried Spicy Pork Bulgogi, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원) |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

<a id="day-wed"></a>
### 수(09/16)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | 🌄 **아침 (조식)**: 해물짬뽕탕 Spicy Seafood Soup (1,000원), 쌀밥, 미트볼카레라이스 Meatball Curry Rice (1,000원), 우동국<br>🌄 **조식자율바**: 청포묵김가루무침, 간장궁채절임, 배추김치<br>**탕맛기픈**: 부대찌개 Budae Jjigae (Korean Army Stew) (5,500원), 닭매운찜 Spicy Braised Chicken (6,000원)<br>**동방식객 /모던키친**: 새우튀김우동& 핫도그\*케찹 Udon with Fried Shrimp & Hot Dog (6,500원), 치킨난반 Chicken Nanban (5,700원)<br>**공통메뉴**: 쌀밥, 그린샐러드&오리엔탈D<br>**샐러드바**: 오복지, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (5,700원), 해장라면 Bean Sprout& Dried Pollack Ramen (5,700원), 자파게티 Noodles with Black Soybean Sauce (5,700원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (5,700원), 폭탄주먹밥(햄) Rice Ball (Ham) (5,700원), 폭탄주먹밥(참치) Rice Ball (Tuna) (5,700원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (5,700원), 즉석철판떡볶이 Stir-fried Rice Cake (5,700원), 닭강정 Sweet and Sour Chicken (5,700원), 공기밥 Rice (5,700원), 치즈사리 Add ( Cheese) (5,700원), 떡사리 Add ( Rice cake) (5,700원), 날계란사리 Add ( Raw Egg ) (5,700원) |
| 연세대학교 한경관(어울샘) | ☀️ **1층 중식**: 감자탕, 동그랑땡전, 야채묵무침, 오이지무침, 콩자반, 계란후라이, 김치, 숭늉 Gamjatang (Pork Bone Stew), Donggeurangttaeng (Korean Meat Pancakes), Seasoned Jelly and Vegetables, Seasoned Pickled Cucumber, Sweet Braised Black Soybeans, Fried Egg, Kimchi, Sungnyung (Traditional Scorched Rice Tea (7,900원)<br>☀️ **2층 중식**: 국, 게살스프, 대패삼겹두부조림, 아마트리치아나파스타, 제육불고기, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Crab Meat Soup, Braised Tofu with Thinly Sliced Pork Belly, Amatriciana Pasta, Stir-fried Spicy Pork Bulgogi, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원)<br>🌛 **2층 석식**: 국, 게살스프, 곱창부대볶음, 탄탄파스타, 제육불고기, 햄버섯야채솥밥, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Crab Meat Soup, Stir-fried Beef Intestines and Budae-jjigae Ingredients, Dan Dan Pasta, Stir-fried Spicy Pork Bulgogi, Mushroom and Ham Vegetable Stone Pot Rice, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원) |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

<a id="day-thu"></a>
### 목(09/17)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | 🌄 **아침 (조식)**: 육개장 Yukgaejang (Spicy Beef Soup) (1,000원), 쌀밥, 고기산적와사비마요덮밥 Beef Skewers with Wasabi Mayo over Rice (1,000원), 우동국<br>🌄 **조식자율바**: 환어묵곤약조림, 그린샐러드&오리엔탈D, 배추김치<br>**탕맛기픈**: 순살감자탕 Boneless Pork Rib Soup (6,200원), 사골떡만둣국 Beef Bone Soup with Rice Cakes & Dumplings (5,300원)<br>**동방식객 /모던키친**: 잔치국수 & 소떡소떡\*케찹 Noodles in Clear Broth& Sausage–Rice Cake Skewers (6,500원), 제육덮밥 Spicy Pork over Rice (5,800원)<br>**공통메뉴**: 쌀밥, 미역줄기볶음<br>**샐러드바**: 고춧잎무침, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (5,800원), 해장라면 Bean Sprout& Dried Pollack Ramen (5,800원), 자파게티 Noodles with Black Soybean Sauce (5,800원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (5,800원), 폭탄주먹밥(햄) Rice Ball (Ham) (5,800원), 폭탄주먹밥(참치) Rice Ball (Tuna) (5,800원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (5,800원), 즉석철판떡볶이 Stir-fried Rice Cake (5,800원), 닭강정 Sweet and Sour Chicken (5,800원), 공기밥 Rice (5,800원), 치즈사리 Add ( Cheese) (5,800원), 떡사리 Add ( Rice cake) (5,800원), 날계란사리 Add ( Raw Egg ) (5,800원) |
| 연세대학교 한경관(어울샘) | ☀️ **1층 중식**: 미역국, 삼겹김치찜, 온두부양념장, 온모밀, 볼어묵곤약조림, 멸치볶음, 계란후라이, 김치, 숭늉 Seaweed Soup, Braised Kimchi with Pork Belly, Warm Tofu with Seasoned Soy Sauce, Warm Buckwheat Soba, Braised Fish Cakes and Konjac, Stir-fried Anchovies, Fried Egg, Kimchi, Sungnyung (Traditional Scorched Rice Tea) (7,900원)<br>☀️ **2층 중식**: 국, 카레덮밥, 닭다리살김치볶음, 볶음짜장면, 제육불고기, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Curry Rice Bowl, Stir-fried Chicken Thigh with Kimchi, Stir-fried Jajangmyeon, Stir-fried Spicy Pork Bulgogi, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원)<br>🌛 **2층 석식**: 국, 카레덮밥, 모듬튀김, 제육고추장크림파스타, 제육불고기, 햄버섯야채솥밥, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Curry Rice Bowl, Assorted Tempura/Fried Fritters, Spicy Pork Gochujang Cream Pasta, Stir-fried Spicy Pork Bulgogi, Mushroom and Ham Vegetable Stone Pot Rice, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원) |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

<a id="day-fri"></a>
### 금(09/18)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | 🌄 **아침 (조식)**: 김치왕만두전골 Kimchi & Large Dumpling Hot Pot (1,000원), 쌀밥<br>🌄 **조식자율바**: 쥐어채볶음, 숙주나물, 배추김치<br>**탕맛기픈**: 순두부찌개 Soft Tofu Stew (5,000원), 매운돈갈비찜 Spicy Braised Pork Ribs (6,000원)<br>**동방식객 /모던키친**: 차돌쌀국수&춘권 Rice Noodle Soup with Beef Brisket & Spring Rolls (6,500원), 햄김치덮밥&오버이지후라이 Ham & Kimchi Rice with Over-easy Egg (5,700원)<br>**공통메뉴**: 쌀밥, 감자채볶음<br>**샐러드바**: 콩조림, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (5,700원), 해장라면 Bean Sprout& Dried Pollack Ramen (5,700원), 자파게티 Noodles with Black Soybean Sauce (5,700원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (5,700원), 폭탄주먹밥(햄) Rice Ball (Ham) (5,700원), 폭탄주먹밥(참치) Rice Ball (Tuna) (5,700원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (5,700원), 즉석철판떡볶이 Stir-fried Rice Cake (5,700원), 닭강정 Sweet and Sour Chicken (5,700원), 공기밥 Rice (5,700원), 치즈사리 Add ( Cheese) (5,700원), 떡사리 Add ( Rice cake) (5,700원), 날계란사리 Add ( Raw Egg ) (5,700원) |
| 연세대학교 한경관(어울샘) | ☀️ **1층 중식**: 무어묵국, 꽈리고추불고기, 어묵콩나물찜, 볶음짜장면, 가지나물, 콩자반, 게란후라이, 김치 숭늉 Radish and Fish Cake Soup, Stir-fried Bulgogi with Shishito Peppers, Braised Fish Cake and Bean Sprouts, Stir-fried Jajangmyeon, Seasoned Eggplant, Sweet Braised Black Soybeans, Fried Egg, Kimchi, Sungnyung (Traditional Scorched Rice Tea) (7,900원)<br>☀️ **2층 중식**: 국, 짜장덮밥, 곱창부대볶음, 닭고기로제파스타, 제육불고기, 햄버섯야채솥밥, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Jajangmyeon Rice Bowl (Black Bean Paste Rice Bowl), Stir-fried Beef Intestines and Budae-jjigae Ingredients, Chicken Rosé Pasta, Stir-fried Spicy Pork Bulgogi, Mushroom and Ham Vegetable Stone Pot Rice, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원)<br>🌛 **2층 석식**: 국, 짜장덮밥, 대패삼겹두부조림, 닭고기로제파스타, 제육불고기, 샐러드/쌈야채, 계란후라이, 숙주볶음, 김치, 단무지무침, 숭늉 Soup, Jajangmyeon Rice Bowl (Black Bean Paste Rice Bowl), Braised Tofu with Thinly Sliced Pork Belly, Chicken Rosé Pasta, Stir-fried Spicy Pork Bulgogi, Salad / Sliced Cabbage and Lettuce for Wraps, Fried Egg, Stir-fried Mung Bean Sprouts, Kimchi, Seasoned Pickled Radish, Sungnyung (Traditional Scorched Rice Tea) (7,000원) |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

<a id="day-sat"></a>
### 토(09/19)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | **동방식객 /모던키친**: 나주곰탕 Naju Gomtang (Beef Bone Soup) (6,000원), 등심돈가스정식 Pork Loin Cutlet Set (6,200원)<br>**공통메뉴**: 쌀밥, 고추장멸치조림<br>**샐러드바**: 모듬채소절임, 배추김치, 우동국<br>**마이보글**: 라면 Ramen (6,200원), 해장라면 Bean Sprout& Dried Pollack Ramen (6,200원), 자파게티 Noodles with Black Soybean Sauce (6,200원), 불닭볶음면&치즈 Hot Chicken Flavor Ramen (6,200원), 폭탄주먹밥(햄) Rice Ball (Ham) (6,200원), 폭탄주먹밥(참치) Rice Ball (Tuna) (6,200원), 모둠튀김 Deep fried Food Set (Vegetables / Glass Noodles in Seaweed / Deep fried Sweet potato / Fried Dumplings) (6,200원), 즉석철판떡볶이 Stir-fried Rice Cake (6,200원), 닭강정 Sweet and Sour Chicken (6,200원), 공기밥 Rice (6,200원), 치즈사리 Add ( Cheese) (6,200원), 떡사리 Add ( Rice cake) (6,200원), 날계란사리 Add ( Raw Egg ) (6,200원) |
| 연세대학교 한경관(어울샘) | - |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |

<a id="day-sun"></a>
### 일(09/20)

| 식당 | 메뉴 |
|---|---|
| 연세대학교 맛나샘 | - |
| 연세대학교 한경관(어울샘) | - |
| 세브란스 종합관 | - |
| 세브란스 제중관 | - |
