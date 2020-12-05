let arr = [-23, 4, -1, 5, -32]; // №1

let result = arr.filter(function(elem) {
	if (elem > 0) {
		return true;
	} else {
		return false;
	}
});

console.log(result);


let arr2 = [-212, 11, 20, -1, 34, -3]; // №2

let result2 = arr2.filter(function(elem) {
	if (elem < 0) {
		return true;
	} else {
		return false;
	}
});

console.log(result2);


let arr3 = [-1, 0, -2, 3, 6, 5, 10, 33]; // №3

let result3 = arr3.filter(function(elem) {
	if (elem > 0  && elem < 10) {
		return true;
	} else {
		return false;
	}
});

console.log(result3);


let arr4 = ['stop!', 'klock', 'who', 'antonsha', 'tre']; // №4

let result4 = arr4.filter(function(elem){
	if(elem.length > 5) {
		return true;
	} else {
		return false;
	}
});

console.log(result4);


let arr5 = [ 0, 1, 6, 3, 4, 20, 4]; // №5

let result5 = arr5.filter(function(elem, index) {
	if ((elem * index) < 30) {
		return true;
	} else {
		return false;
	}
});

console.log(result5);


let arr6 = [0, 3, [1, 5], 23, [4, 2], 25, [3, 6]]; // №6

let result6 = arr6.filter(function(elem){
	if(Array.isArray(elem)) {
		return false;
	} else {
		return true;
	}
});

console.log(result6);


let arr7 = [-12, -125, -123, 20, -3, 1, 9, 5]; // №7

let result7 = arr7.filter(function(elem){
	if(elem < 0 ) {
		return true;
	} else {
		return false;
	}
});

console.log(result7.length);