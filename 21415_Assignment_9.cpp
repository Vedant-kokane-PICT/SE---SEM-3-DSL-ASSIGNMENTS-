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

class stack{
  int top;  
  char s[m];
  public:
  stack(){
      top = -1;
  }
  
  bool empty(){
      if (top==-1){
          return 1;
      }
      return 0;
  }
  
  bool full(){
      if(top == m- 1){
          return 1;
      }
      return 0;
  }
  char top1(){
      return s[top];
  }
  
  void push(char x){
      if(full()){
          cout<<"Full"<<endl;
          return;
      }
      else{
          top++;
          s[top] = x;
      }
  }
  
  void pop(){
      if(empty()){
          cout<<"Empty"<<endl;
          return;
      }
      else{
          top--;
      }
  }
};



int main(){
    stack s1;
    string s;
    cout<<"Enter a expression"<<endl;
	getline(cin,s);
    for(int i=0;i<s.length();i++){
	    if(s1.empty()){
		s1.push(s[i]);
	    }
	    else if((s1.top1() == '(' && s[i] == ')') || (s1.top1() == '{' && s[i] == '}') ||(s1.top1() == '[' && s[i] == ']')){
		s1.pop();
	    }
	    else if(s[i] == '(' || s[i] == '{' || s[i] == '['){
		s1.push(s[i]);
	    }
    }
    
    if(s1.empty()){
    	cout<<"Well parenthesized expression"<<endl;
	}
    else{
	cout<<"Not a Well parenthesized expression"<<endl;
    }
    return 0;
}

// Example - (A+(B*C)
// Example - (A+(B*C))
