In any language program mostly syntax error occurs due to
unbalancing delimiter such as (),{},[]. Write C++ program using
stack to check whether given expression is well parenthesized or
not.

//============================================================================
// Name        : 21415_Assignment_8.cpp
// Author      : Vedant Kokane
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// 21415 - Vedant Kokane

#include <iostream>
#include <string.h>
using namespace std;

#define m 10

class Stack{
private :
	int top;
	char s[m];

public:
	Stack(){
		top = -1;
	}
	void push(char x){
		if(top == m-1){
			cout<<"Stack is full"<<endl;
		}
		else{
			top++;
			s[top] = x;
		}
	}

	void pop(){
		if(is_empty()){
			cout<<"Stack is empty"<<endl;
		}
		else{
			top--;
		}
	}
	bool is_empty(){
		if(top == -1){
			return 1;
		}
		else{
			return 0;
		}
	}

	bool is_full(){
		if(top == m-1){
			return 1;
		}
		else{
			return 0;
		}
	}
	
	char top1(){
	    return s[top];
	}
};

int main() {
	string s;
	cout<<"Enter a expression"<<endl;
	getline(cin,s);
	int n = s.length();
	Stack s1;
	if(s[0]==')' || s[0]=='}' || s[0]==']'){
		cout<<"Not a Well parenthesized expression"<<endl;
		return 0;
	}
	else{
		int i = 0;
		while(i<n){
			switch(s[i]){
			case '(':
				s1.push(s[i]);
				break;

			case '{':
				s1.push(s[i]);
				break;

			case '[':
				s1.push(s[i]);
				break;
			case ')':
			    if(s1.top1() == '('){
				s1.pop();
			    }
				break;
			case '}':
				if(s1.top1() == '{'){
				s1.pop();
			    }
				break;
			case ']':
				if(s1.top1() == ']'){
				s1.pop();
			    }
				break;
			}
			i++;
		}
	}

	if(s1.is_empty()){
		cout<<"Well parenthesized expression"<<endl;
	}
	else{
		cout<<"Not a Well parenthesized expression"<<endl;
	}
	return 0;
}

// Example - (A+(B*C)
// Example - (A+(B*C))
