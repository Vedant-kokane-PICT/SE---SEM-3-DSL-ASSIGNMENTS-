//============================================================================
// Name        : 21415_Assignment_13.cpp
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

class Dequeue{
    private:
    int front;
	int rear;
    int deque_array[m];


	public:

    Dequeue(){
        front = -1;
        rear = -1;

    }

    void insert_front(int x){
        if(is_empty()){
            front++;
            rear++;
            deque_array[rear] = x;
        }
        else if(is_full()){
            cout<<"Full"<<endl;
            return ;
        }
        else{
            for(int i=rear; i>=0; i--){
                deque_array[i+1] = deque_array[i];
            }
            deque_array[0] = x;
            rear++;
        
        }
    }

    void  insert_rear(int x){
        if(is_empty()){
            front++;
            rear++;
            deque_array[rear] = x;
        }
        else if(is_full()){
            cout<<"Full"<<endl;
            return;
        }
        else{
            rear++;
            deque_array[rear] = x;
        }
    }

    void delete_front(){
		if(front == -1 || front == rear+1){
			return;
		}
		else{
			front++;
		}
	}

    void delete_rear(){
        if(is_empty()){
            cout<<"Empty"<<endl;
            return;
        }
        else{
            if(front == rear){   // if only 1 element
                front = -1;
                rear = -1;
            }
            rear--;
        }
    }

	bool is_empty(){
		if(front == -1 || front == rear +1){
			return 1;
		}
		return 0;
	}

    bool is_full(){
		if(rear == m-1){
			return 1;
		}
		return 0;
	}

    void display_front(){
        cout<<deque_array[front]<<endl;
    }

    void display_rear(){
        cout<<deque_array[rear]<<endl;
    }
};

int main(){
    Dequeue d1;
    char c = 'y';
    int x;
    while(c != 'n'){
        cout<<"1. Insert an element from front"<<endl;
        cout<<"2. Insert an element from rear"<<endl;
        cout<<"3. Delete an element from front"<<endl;
        cout<<"4. Delete an element from rear"<<endl;
        cout<<"5. Display front element"<<endl;
        cout<<"6. Display rear element"<<endl;
        int choice;
        cin>>choice;
        switch (choice)
        {
        case 1:
            cout<<"Enter an element"<<endl;
            cin>>x;
            d1.insert_front(x);
            break;
        case 2:
            cout<<"Enter an element"<<endl;
            cin>>x;
            d1.insert_rear(x);
            break;
        case 3:
            d1.delete_front();
            break;
        case 4:
            d1.delete_rear();
            break;
        case 5:
            d1.display_front();
            break;
        case 6:
            d1.display_rear();
            break;
        default:
            break;
        }
        cout<<"Do you want to try any other operation (y/n)"<<endl;
        cin>>c;
    }
    return 0;
}
