Queues are frequently used in computer programming, and a
typical example is the creation of a job queue by an operating
system. If the operating system does not use priorities, then
the jobs are processed in the order they enter the system.
Write C++ program for simulating job queue. Write
functions to add job, display job and delete job from queue.

//============================================================================
// Name        : 21415_Assignment_11.cpp
// Author      : Vedant Kokane
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// 21415 - Vedant Kokane
	
#include <iostream>
#include<string.h>
using namespace std;
#define m 10

class Queue{
	string queue_array[m];
	int front;
	int rear;
public:
	Queue(){
		front = -1;
		rear = -1;
	}

	void insert(string x){
		if(rear == m-1){
			cout<<"Queue is Full"<<endl;
		}
		else if(front == -1){
			front = 0;
		}
		else{
			rear++;
			queue_array[rear] = x;
		}
	}
	bool is_empty(){
		if(front==-1 && rear==-1){
			return 1;
		}
		else{
			return 0;
		}
	}
	string pop(){
		if(is_empty()){
			cout<<"Queue is Empty"<<endl;
			return "-1";
		}
		else{
			if(front == rear){
				front = -1;
				rear = -1;
			}
			else{
			string a = queue_array[front];
			front++;
			return a;
			}
		}
	}

	string show_front(){
		cout<<queue_array[front]<<endl;
		return queue_array[front];
	}

	string show_rear(){
		cout<<queue_array[rear]<<endl;
		return queue_array[rear];
	}

	void show_all(){
		if(front == -1){
			cout<<"Queue is Empty"<<endl;
		}
		else{
			for(int i=front;i<=rear;i++){
				cout<<queue_array[i]<<" ";
			}
			cout<<endl;
		}
	}

};

int main() {
	Queue q;
	char c = 'y';
	while(c != 'n'){
		cout<<"1. Add job"<<endl;
		cout<<"2. Delete job"<<endl;
		cout<<"3. Display first job"<<endl;
		cout<<"4. Display last job"<<endl;
		cout<<"5. Display all Jobs"<<endl;
		int choice;
		cin>>choice;
		if(choice == 1){
			string s;
			cout<<"Enter Job - "<<endl;
			cin>>s;
			q.insert(s);
		}
		else if(choice == 2){
			q.pop();
		}
		else if(choice == 3){
			q.show_front();
		}
		else if(choice == 4){
			q.show_rear();
		}
		else if(choice == 5){
			q.show_all();
			cout<<endl;
			string s1 = q.show_front();
			string s2 = q.show_rear();
			cout<<"First job - "<<s1<<endl;
			cout<<"Last job - "<<s2<<endl;
		}
		cout<<"Do you want to continue (y/n)"<<endl;
		cin>>c;
	}
	return 0;
}
