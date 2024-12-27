#include <bits/stdc++.h>
using namespace std;

vector<int> ans;

struct suffix_array {
    string str;
    vector<int> suff_arr, rank, tmp_rank;

    suffix_array(const string& s) {
        str = s;
        int size = s.size();
        suff_arr.resize(size);
        rank.resize(size);
        tmp_rank.resize(size);

        for (int i = 0; i < size; i++) {
            suff_arr[i] = i;
            rank[i] = str[i];
        }

        for (int k = 1; k < size; k *= 2) {
            auto comp = [&](int i, int j) {
                if (rank[i] != rank[j]) {
                    return rank[i] < rank[j];
                }
                int x = (i + k < size) ? rank[i + k] : -1;
                int y = (j + k < size) ? rank[j + k] : -1;
                return x < y;
            };

            sort(suff_arr.begin(), suff_arr.end(), comp);

            tmp_rank[suff_arr[0]] = 0;
            for (int i = 1; i < size; i++) {
                tmp_rank[suff_arr[i]] = tmp_rank[suff_arr[i - 1]] + (comp(suff_arr[i - 1], suff_arr[i]) ? 1 : 0);
            }
            rank = tmp_rank;
        }
    }

    void query(string sub_string) {
        auto low = lower_bound(suff_arr.begin(), suff_arr.end(), sub_string, [&](int index, const string& sub_string) {
            return str.compare(index, sub_string.size(), sub_string) < 0;
        });
        auto high = upper_bound(suff_arr.begin(), suff_arr.end(), sub_string, [&](const string& sub_string, int index) {
            return sub_string < str.substr(index, sub_string.size());
        });

        for (auto pointer = low; pointer != high; ++pointer) {
            ans.push_back(*pointer);
        }
    }
};

int main() {
    string s;
    getline(cin, s);
    s += '$'; 

    suffix_array suffixArray(s);

    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string sub_string;
        getline(cin, sub_string);

        suffixArray.query(sub_string);
    }

    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }

    return 0;
}