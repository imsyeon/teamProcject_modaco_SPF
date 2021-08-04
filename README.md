# teamProcject_modaco_SPF
팀 프로젝트_모두 다같이 코딩(모다코)_주가예측(Stock Price Forecast)



##프로젝트 계획

------------
> 제로 금리시대가 도래하면서 사람들은 주식투자에 많은 관심을 갖게 됐습니다. 
> 주식투자에서 특히 향후 주식 시장 시장전망을 가장 알고 싶어하는 정보로  10% ~ 30%인 수익을 
> 기대한다는것을 한경비즈니스 설문조사에서 나왔습니다.
 
####계획을 통해 구현할 목록
* 과거 데이터를 분석해서 예측을 차트 구현
* 경제 뉴스 
* 주식 종목 시가총액 순위
* KOSPI, KOSDAQ 일별시세 
* 증권사에서 제공하는 종목분석 리포트 
* QnA게시판, 공지사항게시판(로그인 했을경우에만 쓰기, 읽기, 삭제 가능)
* 회원가입, 로그인, 로그아웃

 
## 프로젝트 환경설정

-----------------------
* python, Pycharm 설치
    * pycharm에서 setting >project:프로젝트명>설정>Location에 프로젝트주소/venv(가상환경)>ok하고 터미널에서 가상환경venv실행된 곳에서 pip를 통해 다운받는다.
* pip install Django : python 프레임워크, MTV(Model-Template-View) 패턴을 사용하여  더 적은 코드로 더 신속하게 개발
* pip install Pillow :파이썬에 이미지 처리하기 위한 라이브러리
* pip install django-crispy forms : 게시판에서 폼이 한쪽으로 치우쳐져 있는 모양을 수정(폼이 가로화면 전체로 바뀜)
* pip install django-markdownx : 마크다운 설치, 공지사항에서 마크다운 적용
* pip install django-allauth : 구글, 카카오톡, 페이스북 등 로그인하는 기능을 손쉽게 할 수 있도록 구현
* pip install beautifulsoup4 : HTML로 나타나는 페이지의 요소를 쉽게 다룰 수 있는 도구(타이틀, 버튼 등에 써있는 내용은 무엇인지)
웹 스크레이핑 라이브러리, HTML과 XML 파일로부터 데이터를 추출하는 데 사용된다. 네이버 증권에서 크롤링기 위해서 사용.
* pip install requests : HTTP 프로토콜을 이용하여 웹에서 리소스를 가져오거나, HTTP 패킷을 직접 만들어서 전송할 수 있다.
* pip install lxml : 파서 중 속도가 빠르고, 유연한 파싱이 가능하도록한다.
* pip install urllib3 : URL 작업을 위한 여러 모듈을 모은 패키지
    

## 구현한 기능 설명

-----------------------
1. HOME
    * 경제 뉴스에서 최신 뉴스 3개를 카드형식으로 보여줌 
    * 카드를 누르면 해당 뉴스로 이동
    * 전체적인 화면구성을 bootstrap을 이용하여 반응형 웹과 내비바 등 기능 구현.  
    * index 앱에서 구현.
    

   ![Home](https://user-images.githubusercontent.com/86580625/128129753-88c450e6-73a3-4206-9587-978dd3b2d636.jpg)

###
2. 국내증시
    * sidebar를 통해 메뉴 제공
    * KOSPI와 KOSDAQ 시세와 시가총액을 네이버증권에서 크롤링(parser)을 통해 DB에 저장하고
    저장한 시세들을 테이블로 제공
    * 종목분석 리포트를 네이버증권에서 크롤링하여 DB에 저장하고 저장한 시세를 테이블로 제공. 
      첨부파일을 클릭하면 pdf 파일을 띄우는 기능 구현
    * stock 앱에서 parser를 통해 크롤링하고 DB에 저장하고 국내증시 기능들을 구현.  
    ####
   ![stock](https://user-images.githubusercontent.com/86580625/128130046-0868f7a2-b6bd-463a-bcac-308e546ff638.jpg)  

###
3. 뉴스
    * 네이버 경제 뉴스를 제목과 링크를 크롤링을 통해 DB에 저장하고 테이블로 제공.
    * 제목을 누르면 해당 뉴스로 이동한다.
    * news_data 앱에서 뉴스 기능들을 구현.
    ####
![news](https://user-images.githubusercontent.com/86580625/128130168-4c204a8b-7e68-4d0a-a962-743add886db2.jpg)

###
4. 주식분석
    * 주식 과거 데이터에서 예측 결과를 분석한 테이터를 json으로 저장
    * 삼성, LG, 카카오, sk 하이닉스, 카카오, 현대 종목 별로 
      1개월, 6개월, 1년, 2년, 3년을 chart.js를 이용하여
      차트로 예측값과 종가를 보여주는 기능을 구현.
    * index앱에서 이 기능들을 구현.
    #####
![chart](https://user-images.githubusercontent.com/86580625/128130665-68ffe940-7c6b-481b-9860-2e0af6e84e4c.jpg)

###  
5. 고객센터
    * 공지사항
      * 쓴 사람이 로그인해야 삭제, 수정이 가능하고 로그인해야만 글등록이 가능.
      * 마크다운 기능
      * 파일 업로드 가능하고 파일이 업로드 돼있으면 하단에 파일 다운로드 표시 기능 구현.
      * 이미지 업로드가 가능하고 이미지가 있을경우에만 상단에 이미지가 나타나는 기능 구현.
      * 게시글이 5개 미만인경우 페이징이 나타나지 않는 기능 구현.
      * notice 앱에서 기능들을 구현.
    
    ####
![notice](https://user-images.githubusercontent.com/86580625/128130788-0e9ad5f6-e384-4dde-a711-e38d1692cb67.jpg)
    * 고객 게시판
      * 로그인을 해야만 글등록, 답글, 수정, 삭제, 댓글, 대댓글을 쓸 수 있도록 구현.
      * 댓글이 있는경우 게시판 리스트에 표시하는 기능 구현.
      * 수정한 날짜 기능 구현
      * customer_board에서 기능 구현
    ####
![QnA](https://user-images.githubusercontent.com/86580625/128130844-88700b5f-1d6c-4a89-a4c4-27156cc0b9fc.jpg)

###    
6. 회원가입, 로그인, 로그아웃
    * common에서 기능을 구현
   #### 
![login](https://user-images.githubusercontent.com/86580625/128131004-386674d2-330f-424d-b599-8a4cfce09e87.jpg)


## 외부 리소스, 출처 및 참고문헌
________
1. 구글 API : 구글아이디로 로그인
2. bootstrap
3. fontawesome : icon 이미지 가져오기
4. http://hangul.thefron.me/ : 게시판 테스트를 위해 장문의 글이 생성되는 사이트
4. 네이버증권 : 국내증시 정보 크롤링
5. 야후 증권 : 과거데이터를 통해 예측 분석
6. 점프 투 장고
7. 장고+부트스트랩 파이썬 웹개발의 정석
    


