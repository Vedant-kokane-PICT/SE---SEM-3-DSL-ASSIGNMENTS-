Implement C++ program for expression conversion as infix to
postfix and its evaluation using stack based on given
conditions: 1. Operands and operator, both must be single
character. 2. Input Postfix expression must be in a desired
format. 3. Only '+', '-', '*' and '/ ' operators are expected.

//============================================================================
// Name        : 21415_Assignment_10.cpp
// Author      : Vedant Kokane
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

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
	char top_of_stack(){
		return s[top];
	}

	int top_int(){
		return s[top];
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
};


int precedence(char x){
	if(x == '^'){
		return 3;
	}
	else if(x == '/' || x == '*'){
		return 2;
	}
	else if(x == '+' || x == '-'){
		return 1;
	}
	return 0;
}

void evaluate(string postfix){
	Stack st;
	for (int i = 0; postfix[i]; ++i)
    {
        if (isdigit(postfix[i]))
            st.push(postfix[i] - '0');
        else
        {
            int val1 = st.top_int();
			st.pop();
			int val2 = st.top_int();
            switch (postfix[i])
            {
            case '+': 
		st.push(val2 + val1);
		break;
            case '-':
		st.push( val2 - val1);
		break;
            case '*':
		st.push(val2 * val1); 
		break;
            case '/': 
		st.push(val2/val1);
		break;
            }
        }
    }
	cout<<st.top_int()<<endl;
}

int main() {
	string s;
	cout<<"Enter a expression"<<endl;
	getline(cin,s);
	int n = s.length();
	Stack st;
	string post_fix = "";
	for(int i=0;i<n;i++){
		char ch = s[i];
		// if there is operand then it will be added to the post_fix string
		if((ch >='a' && ch <= 'z') || (ch >='A' && ch <= 'Z') || (ch >='0' && ch <= '9')){
			post_fix = post_fix  + ch;
		}
		// for checking opening brackets
		else if((ch == '(') || (ch == '[') || (ch == '{')){
			st.push(ch);
		}
		// for checking closing brackets
		else if((ch == ')')|| (ch == ']') || (ch == '}')){
			if(ch==')'){
				while(st.top_of_stack() != '('){
					post_fix = post_fix + st.top_of_stack();
					st.pop();
			}
				st.pop(); // for popping (
			}
			if(ch==']'){
				while(st.top_of_stack() != '['){
					post_fix = post_fix + st.top_of_stack();
					st.pop();
			}
				st.pop(); // for popping [
			}
			if(ch=='}'){
				while(st.top_of_stack() != '{'){
					post_fix = post_fix + st.top_of_stack();
					st.pop();
				}
				st.pop(); // for popping {
			}
		}
		// for checking operator
		else{
			while((!st.is_empty()) && (precedence(ch) <= precedence(st.top_of_stack()))){
				post_fix = post_fix + st.top_of_stack();
				st.pop();
			}
			st.push(ch);
		}
	}
	while(!st.is_empty()){
		post_fix = post_fix + st.top_of_stack();
		st.pop();
	}

	cout<<post_fix<<endl;

	cout<<"Evaluate - (y/n)"<<endl;
	char e;
	cin>>e;
	if(e=='y'){
		evaluate(post_fix);
	}
	return 0;
}

/*
 Examples -
A+B
A+B*C
(A+B)*C
{[a+b]+(c/d)}
*/



