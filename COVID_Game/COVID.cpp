#include <bits/stdc++.h>
#include <ctime>
#include <vector>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <gdiplus.h>
using namespace std;

const int RED = 12;
const int BLUE = 9;
const int GREEN = 10;
const int WHITE = 15;
const int PURPLE = 13;
char board[17][17];
vector<int> Z[40];
vector<int> V[40];
vector<int> A[40];
bool New_Game = false, Exit= false, Go_To_Menu = true, flag1 = true, flag2 = true, flag3 = true, Levelup = false, zombie_range;
int x = 1, y = 1, Round = 0, Level = 1, Credit = 0, Vaccine = 0, Health = 3, Ammo_Capacity = 3, Current_Ammo = 1, Kill = 0, shutgun_range = 5;
void gotoxy(int x, int y) {
	COORD coord;
	coord.X = x;
	coord.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void delay(int millisecond) {
	Sleep(millisecond);
}

void clear() {
	system("cls");
}

void init() {
	x = 1, y = 1;
	Vaccine = 0;
	Health = 3;
	Credit = 0;
	Level = 1;
	Round = 0;
	Kill = 0;
	flag1 = true, flag2 = true, flag3 = true, Exit = false;
	Current_Ammo = 3;
	Ammo_Capacity = 3;
	for (int i = 0; i < 40; i++) {
		Z[i].clear();
		V[i].clear();
		A[i].clear();
	}
}

void kill() {
	gotoxy(0, 21);
	int resault = (Kill - 1) % 14;
	switch(resault) {
		case 0 : cout << "First Blood";
		   break;
		case 1 : cout << "Double Kill";
		   break;
		case 2 : 
		if (Round % 2 == 0)
		   cout << "Triple Kill";
		else
		   cout << "Hattrick";
		   break;
		case 3 : cout << "Team Killer";
		   break;
		case 4 : cout << "Headshot";
		   break;
		case 5 : cout << "Rampage";
		   break;
		case 6 : cout << "Killing Spree"; 
		   break;
		case 7 : cout << "Unstoppable";
		   break;
		case 8 : cout << "Monster Kill";
		   break;
		case 9 : cout << "Multi Kill";
		   break;
		case 10 : cout << "Ludicrouskill";
		   break;
		case 11 : cout << "Ultra Kill";
		   break;
		case 12 : cout << "Dominating";
		   break;
		case 13 : cout << "Godlike";  
		   break;                              
	}
}

bool game_over() {
	if (!Health)
	   return true;
	else
	   return false;   
}

void reload() {
	if (Current_Ammo == Ammo_Capacity) {
		gotoxy(0, 20);
		cout << "The gun is already Charged";
		delay(1000);
	}
	else if (Ammo_Capacity) {
		Current_Ammo++;
		Ammo_Capacity--;
		gotoxy(0, 20);
		cout << "Reloaded!";
		delay(1000);
	}
	else if (!Ammo_Capacity) {
		gotoxy(0, 20);
		cout << "No Ammo!";
		delay(1000);
	}
	else if (!Current_Ammo) {
		gotoxy(0, 20);
		cout << "No charged ammo!";
		delay(1000);
	}
}

void danger() {
	if (board[y][x] == 'Z' || board[y][x - 1] == 'Z' || board[y][x + 1] == 'Z' || board[y - 1][x] == 'Z' || board[y - 1][x + 1] == 'Z' || board[y - 1][x - 1] == 'Z' || board[y + 1][x] == 'Z' || board[y + 1][x + 1] == 'Z' || board[y + 1][x - 1] == 'Z') {
		Health--;
		gotoxy(0, 20);
		cout << "The zombie is eating you! You lost one of your healths!";
		delay(1200);
	}
}

void find_Z(int y, int i) {
	for (int j = 0; j < Level; j++) {
		if (Z[2 * Level - 2][j] == y && Z[2 * Level - 1][j] == i) {
			Z[2 * Level - 2][j] = -10000;
			Z[2 * Level - 1][j] = -10000;
		}
	}
}

void find_V(int y, int i) {
	for (int j = 0; j < Level; j++) {
		if (V[2 * Level - 2][j] == y && V[2 * Level - 1][j] == i) {
			V[2 * Level - 2][j] = -10000;
			V[2 * Level - 1][j] = -10000;
		}
	}
}

void find_A(int y, int i) {
	for (int j = 0; j < Level; j++) {
		if (A[2 * Level - 2][j] == y && A[2 * Level - 1][j] == i) {
			A[2 * Level - 2][j] = -10000;
			A[2 * Level - 1][j] = -10000;
		}
	}
}

void zombie_move(int y, int i, int n) {
	for (int j = 0; j < Level; j++) {
		if (Z[2 * Level - 2][j] == y && Z[2 * Level - 1][j] == i) {
			if (n == 0) 
			   Z[2 * Level - 1][j]--;
			else if (n == 1)
			   Z[2 * Level - 1][j]++;
			else if (n == 2)
			   Z[2 * Level - 2][j]++;  
			else if (n == 3)
			   Z[2 * Level - 2][j]--;       
		}
	}
}

void board_game() {
	cout << "Level : " << Level << " Vaccine : " << Vaccine << " Credit : " << Credit << " Round : " << Round << endl;
	cout << "Health : [ ";
	for (int i = 0; i < Health; i++)
	   cout << "| ";
	cout << "]";   
	   cout << " Ammo : " << Ammo_Capacity << "/" << Current_Ammo;
	cout << " Kill : " << Kill << endl;
	for (int i = 0; i < 17; i++) {
		for (int j = 0; j < 17; j++) {
			if (i == 0 || i == 16)
			   board[i][j] = '-';
			else if ((j == 0 || j == 16) && i != 0 && i != 16)
			   board[i][j] = '|';
			else
			   board[i][j] = ' ';      
		}
	}
	board[y][x] = 'P';
	board[15][15] = 'D';
	
	srand(time(NULL));
	if(flag1) {
		int counter1 = 1;
		while(counter1 <= Level) {
		   int a = rand() % 15 + 1;
		   int b = rand() % 15 + 1;
		   if (board[a][b] == ' ' || board[a][b] == 'V' || board[a][b] == 'A') {
		  	   board[a][b] = 'Z';
		  	   Z[2 * Level - 2].push_back(a);
		  	   Z[2 * Level - 1].push_back(b);
			   counter1++;
	 	   } 
	    }
	    flag1 = false;
	}
	
	if (flag2) { 
		int counter2 = 1;
		while(counter2 <= Level) {
		   int a = rand() % 15 + 1;
		   int b = rand() % 15 + 1;
		   if (board[a][b] == ' ' || board[a][b] == 'A') {
		  	   board[a][b] = 'V';
		  	   V[2 * Level - 2].push_back(a);
		  	   V[2 * Level - 1].push_back(b);
			   counter2++;
	 	   } 
	    }
	    flag2 = false;
	}
	
		if (flag3) {
		int counter3 = 1;
		while(counter3 <= Level) {
		   int a = rand() % 15 + 1;
		   int b = rand() % 15 + 1;
		   if (board[a][b] == ' ') {
		  	   board[a][b] = 'A';
		  	   A[2 * Level - 2].push_back(a);
		  	   A[2 * Level - 1].push_back(b);
			   counter3++;
	 	   } 
	    }
	    flag3 = false;
	}
	
	if (!flag1) {
		for (int i = 0; i < Level; i++) {
			if (Z[2 * Level - 2][i] != -10000 && Z[2 * Level - 1][i] != -10000)
			    board[Z[2 * Level - 2][i]][Z[2 * Level - 1][i]] = 'Z';
		}
	}
	
	if (!flag2) {
		for (int i = 0; i < Level; i++) {
			if (V[2 * Level - 2][i] != -10000 && V[2 * Level - 1][i] != -10000)
			    board[V[2 * Level - 2][i]][V[2 * Level - 1][i]] = 'V';
		}
	}
	
	if (!flag3) {
		for (int i = 0; i < Level; i++) {
			if (A[2 * Level - 2][i] != -10000 && A[2 * Level - 1][i] != -10000)
			    board[A[2 * Level - 2][i]][A[2 * Level - 1][i]] = 'A';
		}
	}
	
	for (int i = 0; i < 17; i++) {
		for (int j = 0; j < 17; j++) {
			HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
			if (board[i][j] == 'P') {
			   SetConsoleTextAttribute(hConsole, GREEN);
			   cout << board[i][j];
		    }
		    else if (board[i][j] == 'D') {
		    	SetConsoleTextAttribute(hConsole, PURPLE);
		    	cout << board[i][j];
			}
			else if (board[i][j] == 'Z') {
				SetConsoleTextAttribute(hConsole, RED);
		    	cout << board[i][j];
			}
			else if (board[i][j] == 'A') {
				SetConsoleTextAttribute(hConsole, BLUE);
		       cout << board[i][j]; 
			}
			else { 
			   SetConsoleTextAttribute(hConsole, WHITE);
		       cout << board[i][j]; 
		    }
		}
		cout << "\n";
	}
}

void shoot(char input) {
	if (input == 't') {
		zombie_range = false;
		if (!Current_Ammo) {
			gotoxy(0, 20);
			cout << "No charged ammo!";
			delay(1200);
		}
		else {
		   for (int i = y - 1; i >= y - 5; i--) {
			   if (i == 0)
			      break;
			   else {
				   if (board[i][x] == 'Z'){
					   zombie_range = true;
					   find_Z(i, x);
					   Kill++;
					   Current_Ammo--;
				 	   Credit += Level + 1;
				   }
			   }   
		   }
		   if (zombie_range) {
			   gotoxy(0, 21);
			   cout << Level + 1 << " credit gained!" << endl;
			   kill();
			   delay(1200);
		   }
		   else {
			   gotoxy(0, 21);
			   cout << "Zombie is not in range!Come closer.";
			   delay(1200);
		   }
	   }
	}
	if (input == 'g') {
		zombie_range = false;
		if (!Current_Ammo) {
			gotoxy(0, 20);
			cout << "No charged ammo!";
			delay(1200);
		}
		else {
		   for (int i = y + 1; i <= y + 5; i++) {
			   if (i == 16)
			      break;
			   else {
				   if (board[i][x] == 'Z') {
					   zombie_range = true;
					   find_Z(i, x);
					   Kill++;
					   Current_Ammo--;
					   Credit += Level + 1;
				   }
			   }   
		   }
		   if (zombie_range) {
			   gotoxy(0, 21);
			   cout << Level + 1 << " credit gained!" << endl;
			   kill();
			   delay(1200);
		   }
		   else {
			   gotoxy(0, 21);
			   cout << "Zombie is not in range!Come closer.";
			   delay(1200);
		   }
	   }
	}
	if (input == 'f') {
		zombie_range = false;
		if (!Current_Ammo) {
			gotoxy(0, 20);
			cout << "No charged ammo!";
			delay(1200);
		}
		else {
		   for (int i = x + 1; i <= x + 5; i++) {
			   if (i == 16)
			      break;
			   else {
				   if (board[y][i] == 'Z') {
					   zombie_range = true;
					   find_Z(y, i);
					   Kill++;
					   Current_Ammo--;
					   Credit += Level + 1;
				   }
			   }   
		   }
		   if (zombie_range) {
			   gotoxy(0, 21);
			   cout << Level + 1 << " credit gained!" << endl;
			   kill();
			   delay(1200);
		   }
		   else {
			   gotoxy(0, 21);
			   cout << "Zombie is not in range!Come closer.";
			   delay(1200);
		   }  
	   }
	}
	if (input == 'h') {
		zombie_range = false;
		if (!Current_Ammo) {
			gotoxy(0, 20);
			cout << "No charged ammo!";
			delay(1200);
		}
		else {
		   for (int i = x - 1; i >= x - 5; i--) {
			   if (i == 0)
			      break;
			   else {
				   if (board[y][i] == 'Z') {
					   zombie_range = true;
					   find_Z(y, i);
					   Kill++;
					   Current_Ammo--;
					   Credit += Level + 1;
				   }
			   }   
		   }
		   if (zombie_range) {
			   gotoxy(0, 21);
			   cout << Level + 1 << " credit gained!" << endl;
			   kill();
			   delay(1200);
		   }
		   else {
			   gotoxy(0, 21);
			   cout << "Zombie is not in range!Come closer.";
			   delay(1200);
		   }
	   }
	}
}

void input() {
	if (kbhit()) {
		char key = getch();
		Round++;
		
		if (Round % 2 == 0) {
			for (int i = 1; i < 16; i++) {
			   for (int j = 1; j < 16; j++) {
				   if (board[i][j] == 'Z') {
					   if (x < j) {
						   zombie_move(i, j, 0);
					   }
					   else if (x > j) {
						   zombie_move(i, j, 1);
					   }
					   else if (x == j && y > i) {
						   zombie_move(i, j, 2);
					   }
					   else if (x == j && y < i) {
						   zombie_move(i, j, 3);
					   }
				   }
			   }
		    }
		}
		
		switch(key) {
			case 'w' : 
			if (board[y - 1][x] == 'V') {
				Vaccine++;
				Credit += Level + 1;
				find_V(y - 1, x);
				gotoxy(0, 20);
				cout << "Vaccine collected!" << "\n";
				cout << Level + 1 << " credit gained!";
				delay(1000); 
		    }
		    else if (board[y - 1][x] == 'A') {
		    	Ammo_Capacity++;
		    	find_A(y - 1, x);
		    	gotoxy(0, 20);
		    	cout << "Ammo collected!";
		    	delay(1000);	
			}
			if (y > 1)
		       y--;
			   break;
			case 's' :  
			if (board[y + 1][x] == 'V') {
				Vaccine++;
				Credit += Level + 1;
				find_V(y + 1, x);
				gotoxy(0, 20);
				cout << "Vaccine collected!" << "\n";
				cout << Level + 1 << " credit gained!";
				delay(1000); 
		    }
		    else if (board[y + 1][x] == 'A') {
		    	Ammo_Capacity++;
		    	find_A(y + 1, x);
		    	gotoxy(0, 20);
		    	cout << "Ammo collected!";
		    	delay(1000);
			}
			else if (board[y + 1][x] == 'D') {
				if (Vaccine < Level) {
					gotoxy(0, 20);
					cout << "First get all the vaccines.";
					delay(1200);	
				}
				else if (Vaccine == Level) {
					gotoxy(0, 20);
					cout << "You Won!You have reached level " << Level + 1;
					delay(2000);
					Levelup = true;
				}
			}
			if (y < 15)
			   y++;
			   break;
			case 'd' : 
			if (board[y][x + 1] == 'V') {
				Vaccine++;
				Credit += Level + 1;
				find_V(y, x + 1);
				gotoxy(0, 20);
				cout << "Vaccine collected!" << "\n";
				cout << Level + 1 << " credit gained!";
				delay(1000); 
		    }
		    else if (board[y][x + 1] == 'A') {
		    	Ammo_Capacity++;
		    	find_A(y, x + 1);
		    	gotoxy(0, 20);
		    	cout << "Ammo collected!";
		    	delay(1000);
			} 
				else if (board[y][x + 1] == 'D') {
				if (Vaccine < Level) {
					gotoxy(0, 20);
					cout << "First get all the vaccines.";
					delay(1200);	
				}
				else if (Vaccine == Level) {
					gotoxy(0, 20);
					cout << "You Won!You have reached level " << Level + 1;
					delay(2000);
					Levelup = true;
				}
			}
			if (x < 15)
			   x++;
			   break;
			case 'a' : 
				if (board[y][x - 1] == 'V') {
				Vaccine++;
				Credit += Level + 1;
				find_V(y, x - 1);
				gotoxy(0, 20);
				cout << "Vaccine collected!" << "\n";
				cout << Level + 1 << " credit gained!";
				delay(1000); 
		    }
		    else if (board[y][x - 1] == 'A') {
		    	Ammo_Capacity++;
		    	find_A(y, x - 1);
		    	gotoxy(0, 20);
		    	cout << "Ammo collected!";
		    	delay(1000);
			}
			if (x > 1)
			   x--;
			   break;
			case 'r' : reload();
			   break;   
			case 't' : shoot(key);
			   break;
			case 'g' : shoot(key);
			   break;
			case 'f' : shoot(key);
			   break;
			case 'h' : shoot(key);
			   break;               
			case 'e' : Exit = true; 
			   break;         
		}
		danger();
	}
}

void first_page() {
	char welcome[7][86] = {
	                      {' ', '#', '#', '#', '#','#', '#', ' ', ' ', ' ','#', '#', '#', '#', '#','#', '#', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', '#','#', '#', '#', ' ', '#','#', '#', '#', '#', '#','#', '#', ' ', ' ', ' ',' ', ' ', ' ', '#', '#','#', '#', '#', '#', '#',' ', ' ', ' ', ' ', '#','#', '#', '#', '#', ' ',' ', ' ', ' ', '#', '#','#', '#', '#', '#', '#',' ', ' ', ' ', ' ', '#','#', '#', '#', '#', ' ', ' '},
	                      {'#', '#', ' ', ' ', ' ',' ', '#', '#', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ','#', '#', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', '#', '#',' ', ' ', ' ', '#', '#',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', '#', '#',' ', ' ', ' ', '#', '#', ' '},
	                      {'#', '#', ' ', ' ', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ','#', '#', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', '#','#', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', '#','#', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#', '#'},
	                      {'#', '#', ' ', ' ', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ','#', '#', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ',' ', ' ', ' ', '#', '#','#', '#', '#', '#', '#',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', '#', '#','#', '#', '#', '#', '#',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#', '#'},
	                      {'#', '#', ' ', ' ', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ','#', '#', ' ', ' ', ' ','#', '#', ' ', ' ', ' ','#', '#', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', '#','#', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#', '#'},
	                      {'#', '#', ' ', ' ', ' ',' ', '#', '#', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ',' ', '#', '#', ' ', '#','#', ' ', ' ', ' ', ' ','#', '#', ' ', ' ', '#','#', ' ', ' ', ' ', ' ',' ', '#', '#', ' ', ' ',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', '#', '#',' ', ' ', ' ', '#', '#',' ', ' ', '#', '#', ' ',' ', ' ', ' ', ' ', '#','#', ' ', ' ', '#', '#',' ', ' ', ' ', '#', '#', ' '},
	                      {' ', '#', '#', '#', '#','#', '#', ' ', ' ', ' ','#', '#', '#', '#', '#','#', '#', ' ', ' ', ' ',' ', ' ', '#', '#', '#',' ', ' ', ' ', ' ', '#','#', '#', '#', ' ', '#','#', '#', '#', '#', '#','#', '#', ' ', ' ', ' ',' ', ' ', '#', '#', '#','#', '#', '#', '#', '#','#', ' ', ' ', ' ', '#','#', '#', '#', '#', ' ',' ', ' ', ' ', '#', '#','#', '#', '#', '#', '#',' ', ' ', ' ', ' ', '#','#', '#', '#', '#', ' ', ' '}
	};
	
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 86; j++) {
			SetConsoleTextAttribute(hConsole, RED);
			cout << welcome[i][j];
		}
		cout << endl;
	}
	
	SetConsoleTextAttribute(hConsole, WHITE);
	   cout << "Welcome to Covid 2030 game!" << endl; 
	  
}

void show_setting() {
	cout << "Final level is : 20";
	delay(4000);
	clear();
	Go_To_Menu = true;
	Exit = false;
	New_Game = false;
}

void credits() {
	cout << "Writer : Amin Janani";
	delay(4000);
	clear();
	Go_To_Menu = true;
	Exit = false;
	New_Game = false;
}

void help() {
	cout << "Game Rules :" << endl;
	cout << "To move up press 'w'" << endl;
	cout << "To move down press 's'" << endl;
	cout << "To move to the right press 'd'" << endl;
	cout << "To move to the left press 'a'" << endl;
	cout << "To shoot upwards press 't'" << endl;
	cout << "To shoot downwards press 'g'" << endl;
	cout << "To shoot to the right press 'f'" << endl;
	cout << "To shoot to the left press 'h'" << endl;
	cout << "To reload the gun press 'r'" << endl;
	cout << "To go to upgrade menu press 'u'" << endl;
	delay(10000);
	clear();
	Go_To_Menu = true;
	Exit = false;
	New_Game = false;
}

void exit() {
	cout << "Are you sure you want to exit the game? (n/y)";
	char input = getch();
	if (input == 'n') {
		clear();
		Go_To_Menu = true;
		Exit = false;
		New_Game = false;
	}
	else {
	   Exit = true;
	   Go_To_Menu = false;
	   New_Game = false;
    }
}

void menu() {
	cout << "1 - New Game" << endl;
	cout << "2 - Setting" << endl;
	cout << "3 - Credits" << endl;
	cout << "4 - Help" << endl;
	cout << "5 - Exit" << endl;
	cout << "Please enter a number between 1 and 5" << endl;
	char input = getch();
	clear();
	switch(input) {
		case '1' : New_Game = true;
		   break;
		case '2' : show_setting();
		   break;
		case '3' : credits();
		   break;
		case '4' : help();
		   break;
		case '5' : exit();
		   break;            
	}
}

int main() {
	first_page();
	delay(10000);	
	
	clear();
	do {
		if (Go_To_Menu)
		   menu();
		if (New_Game || Exit) {
			clear();
		   break;
	    }
		
	}while(true);
	
	if (Exit)
	   cout << "********************* Good Bye! *********************";
	else if (New_Game) {
		char key;
		gotoxy(20, 20);
		cout << "*****************************************************";
		gotoxy(0, 0);
		while(!Exit) {
			clear();
			
			if (Level == 21) {
				cout << "Congratuations! You have successfully collected all the vaccines! Now it is time to return to the Earth\nGood Bye!";
				delay(4000);
				clear();
				break;
			}
			
			if (game_over()) {
				cout << "You Died!\nYou Lose!Would you like to try again?(y/n)" << endl;
				char inp = getch();
				if (inp == 'n')
				   break;
				else 
				   init();  
			}
			
			if (Levelup) {
				Level++;
				x = 1, y = 1;
	            Vaccine = 0;
	            Health = 3;
	            Credit = 0;
	            Round = 0;
 	            Kill = 0;
 	            flag1 = true;
 	            flag2 = true;
 	            flag3 = true;
 	            Levelup = false;
			}
			
			board_game();
			
			input();
			
			delay(300);
		}
		clear();
		cout << "********************* Good Bye! *********************"; 
	} 
				  
	return 0;
}