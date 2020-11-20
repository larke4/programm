let arr = [2, 5, 6, 19, 55];//Задание №1

let res = arr.map(function(elem) {
	return Math.sqrt(elem)
});

console.log(res);


let mah = ['Ку','house', 'собака', 'кот', 'чикаго'];//Задание №2

res1 = mah.map(function(elem) {
	return elem + '!'
});
	
console.log(res1);


let str = ['линия','кот', '21', 'ягнята', 'молчание'];//Задание №3

res2 = str.map(function(elem) {
	return elem.split('').reverse().join('')
});

console.log(res2);


let arr2 = ['123', '456', '789'];//Задание №4

let res3 = arr2.map(function(elem) {
	return elem.split('')
});

console.log(res3);


let arr3 = [3, 6, 9, 1, 4];//Задание №5

let res4 = arr3.map(function(elem, index) {
	return elem * index;
});

console.log(res4); 