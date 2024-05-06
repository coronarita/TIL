// CSS 선택자('item')로 검색 - itemEls에 할당
const itemEls = document.querySelectorAll('.item')
const btnEl = document.querySelector('.btn')
const colors = ['royalblue', 'orange', 'tomato']


btnEl.addEventListener('click', function () {
  itemEls.forEach(function (itemEl, index, array) { // 각각의 아이템에 접근해서 실행하는 함수
    console.log(index, itemEl, array)
    itemEl.style.backgroundColor = colors[index]
  })
  btnEl.innerHTML = '<span>클릭했어요!</span>' 

}) // 버튼을 클릭하는 이벤트를 받음

// 이름이 없음 : 익명함수

// querySelector를 통해 찾은 요소에, Style을 통해 css 할당 하거나,
// innerHTML을 통해 html 값 자체를 변경할 수 있음