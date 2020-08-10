#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int main()
{
	map<string,int> m;
	fstream out;
	ofstream outfile;
	out.open("list_id.txt",ios::in);
	outfile.open("list.txt");
	while(!out.eof()){
		char buffer[25];
		out.getline(buffer,25);
		// cout<<buffer<<endl;
		if(buffer[0] == '=') {
			string s;
			for(int i = 1;i < 10;i++) s += buffer[i];
			outfile<<s<<endl;	
		}
		//m[buffer]++;
		else{
			outfile<<buffer<<endl;	
		}
		cout<<buffer<<endl;
	}
//	for(auto it = m.begin();it != m.end();it++){
//		if(it->second > 3) cout<<it->first<<"³öÏÖ"<<it->second<<"´Î"<<endl;
//	}
	outfile.close();
	out.close();
	return 0;
}
