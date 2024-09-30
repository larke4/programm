#include <stdio.h>


void print_menu(){ // МЕНЮ. Вывод пунктов меню.
	int i;
	printf("\nChosse exercise: \n");
	printf("1. Exercise 1 (task 11)\n");
	for (i = 2; i <= 5; i++){
	printf("%d. Exercise %d (task %d)\n", i, i, i+4);
	}

	printf("\nHelp command: \n");
	printf("6. Open this menu again \n");
	printf("7. Exit proggramm \n");
	printf("Enter : ");
}

int ex_choose(){ // МЕНЮ. Выбор пункта меню, проверка на дебила
	char ent;
	scanf("%s", &ent);
	int numb = ent-'0'; // Конструкция перевода из char в int. Хызы, atoi просто не работает, может я тупой.
	while(numb < 1 || numb > 7){
		printf("Incorrect value. Choose exercies 1-7: ");
		scanf("%s", &ent);
		numb = ent-'0';
		printf("%d", numb);
	}
	return numb; // Возвращаем номер выбранного пункта меню
}

void ex1(){ //Первое задание, 11 упражнение
	int k, m, n;
	printf("Программа выводит количество раз, сколько нужно домножить 1 на 2, что бы получить введёное число\n");
	printf("или число больше него на одну итерацию умножения\n");
	printf("Enter number: ");
	scanf("%d", &n);
	for (k = 2, m = 1; m <= n; k++, m = m*2){
		printf("Result: %d \n", k-1);
	}
}

void ex2(){ //Второе задание, 6 упражнение
	int a, n;
	int s = 0;
	printf("Программа выводит ближайшее к 2 число, на которое делиться введёное число без остатка\n");
	printf("Enter number: ");
	scanf("%d", &a);
	for (n=2; n < a; n++){
		if (a%n==0){
			s=1;
			break;
		}
	}
	printf("Result: %d \n", n);
}

void ex3(){ // Третье задание, 7 упражнение
	int n = 2;
	int flag = 0;
	int a;
	printf("Программа выводит ближайшее к 2 или болше двух число, на которое делиться введёное число \n");
	printf("Enter number: ");
	scanf("%d", &a);
	while (a%n != 0){
		if (n == a){
			flag = 1;
			break;
		}
	n++;
	}
	printf("Result: %d\n", n);
}

void ex4(){ // Четвёртое задание, 8 упражнение
	int n;
	int s = 1;
	printf("Программа выводит факториал введёного числа\n");
	printf("Enter number: ");
	scanf("%d", &n);
	for (int i=1; i<=n; i++){
		s = s*i;
	}
	printf("Result: %d \n", s);
}

void ex5(){ // Пятое задание, 9 упражнение
	int n, k;
	int s = 0;
	printf("Программа выводит первую цифру числа и перевёрнутое число\n");
	printf("Etner number :");
	scanf("%d", &n);
	for (n; n != 0; n=n/10){
		k = n%10;
		s = s*10+k;
	}
	printf("Первая цифра числа: %d \nПеревёрнутое число: %d\n", k, s);
}

int main () {
	int exnum;
	print_menu();

	do {
		exnum = ex_choose();

		switch (exnum) {
			case 1:
				ex1();
			case 2:
				ex2();
			case 3:
				ex3();
			case 4:
				ex4();
			case 5:
				ex5();
			case 6:
				print_menu();
		}
	} while (exnum != 7);
}
