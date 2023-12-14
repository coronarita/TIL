// h1에 있는 키워드 콘솔에 출력
const el = document.querySelector('h1')
// 콘솔창에 기록을 남김
console.log(el)

// const, let
// 객체 데이터 : const objData = {
  // key:'value'
// }

// objData.key =>> 'value'

const objectData = {
  key:'value',
  name: 'Heropy',
  age: 85,
  email: ' thesecon@gmail.com'
}
console.log(objectData.email) // 점표기법
console.log(objectData)
console.log(objectData['email']) // 대괄호 접근법

// 배열 데이터
const arrayData = [9, 8, 7, 6] // 대괄호, 쉼표로 구분
console.log(arrayData[0])
console.log(arrayData[1])

let number = 123
console.log(number)
number = 456
console.log(number)

function hello() {
  const message = 'Hello world!'
  console.log(message)
}

hello()
hello()
hello()

function hello2(name){
  if (name.length > 5){
    return
  }
  const message = 'Hello ' + name + '!'
  console.log(message)
  return
  console.log(" 이 부분은 실행되지 않음.. ")  
}
hello2('Heropy')
hello2('Neo')
hello2('Evan')

const message = "Hello World!"
console.log(message)

// DOM(Document Object Model) 

