//背包问题，01背包 参考题目网址：www.acwing.com
//数据输入格式 第一行表示的是物品数量、背包体积
//每行两个整数vi、wi，用空格隔开，分别表示第i件物品的体积和价值

#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

/*
class Soution{
public:
    pkg()
    {   
        int n,m;
        cin >> n>>m;
        const int N = 1010;
        int f[N][N];
        int v[N],w[N];
        for (int i = 1;i<= n;i++) cin>>v[i]>>w[i];
        for (int i = 1; i<= n;i++)
            for(int j = 0; j<= m;j++)
            {
                f[i][j] = f[i-1][j];
                if(j>=v[i]){
                f[i][j] = max(f[i-1][j],f[i-1][j-v[i]]+w[i]);
                }
            }
        int res = 0;
        for (int i =0;i<=m;i++) res = max(res,f[n][i]);
        cout <<res<<endl;
        return 0;


    }

};*/
int n,m;
const int N = 1010;
int f[N][N];
int v[N],w[N];
int main(){

      
        cin >> n>>m;
       
        for (int i = 1;i<= n;i++) cin>>v[i]>>w[i];
        for (int i = 1; i<= n;i++)
            for(int j = 0; j<= m;j++)
            {
                f[i][j] = f[i-1][j];
                if(j>=v[i]){
                f[i][j] = max(f[i-1][j],f[i-1][j-v[i]]+w[i]);
                }
            }
        int res = 0;
        for (int i =0;i<=m;i++) res = max(res,f[n][i]);
        cout <<res<<endl;
        return 0;


}
