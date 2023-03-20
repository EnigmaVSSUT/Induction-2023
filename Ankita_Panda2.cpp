#include<iostream>
using namespace std;
int main(){
    int n,i,j,count=0;
    cin>>n;
    int candles[n];
    
    for(i=0;i<n;i++){
        cin>>candles[i];
    }
     int max=candles[0];
    for(i=0;i<n;i++){
        
        if(max<candles[i])
            max=candles[i];
             
    }
    
    for(i=0;i<n;i++){
        if(candles[i]==max)
             count++;
        
    }
    cout<<count<<endl;
    return 0;
}