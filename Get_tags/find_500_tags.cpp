#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int main()
{
	map<string,int> m;
	fstream out;
	out.open("words.txt",ios::in);
	while(!out.eof()){
		char buffer[256];
		out.getline(buffer,256,',');
		// cout<<buffer<<endl;
		m[buffer]++;
	}
	for(auto it = m.begin();it != m.end();it++){
		if(it->second > 3) cout<<it->first<<"³öÏÖ"<<it->second<<"´Î"<<endl;
	}
	out.close();
	return 0;
}
