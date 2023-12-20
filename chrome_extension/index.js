// 화면상에 있는 이미지들을 네이버 로고로 변환, 링크클릭 시 네이버로 접속하게 하는 코드

// 화면 내에 있는 모든 이미지들을 src에 있는 이미지로 변경해주는 코드
setInterval(() => {
    
    let imgs = document.querySelectorAll("img");
    imgs.forEach((a, i) => {
      a.src = "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbWQq8K%2Fbtrav7cc5Sm%2FciiSK3JSxfBaU3OYJiBTMK%2Fimg.png"
    })
  
    // 화면 내의 링크를 특정 주소로 연결되게 하는 코드

    let urls = document.querySelectorAll("a");
    urls.forEach((a, i) => {
        a.href = "http://naver.com"
    })


  }, 500);

  