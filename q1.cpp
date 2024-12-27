#include <bits/stdc++.h>
using namespace std;

struct node {
    unordered_map<char, node*> children;
    vector<int> values; 
    node* parent;
    char ch;

    node() {
        parent = nullptr;
    }
};

struct suffix_tree {
    node* root;

    suffix_tree() {
        root = new node();
        root->ch = ' ';
    }

    void construct_tree(string s) {
        int size = s.size();
        for (int i = 0; i < size; i++) {
            node* r = root;
            for (int j = i; j < size; j++) {
                if (r->children.find(s[j]) == r->children.end()) {
                    add_child(s[j], i, r);
                }
                r = r->children[s[j]];
                r->values.push_back(i);
            }
        }
    }

    void add_child(char ch, int index, node* parent) {
        node* new_child = new node();
        new_child->ch = ch;
        new_child->parent = parent;
        parent->children[ch] = new_child;
    }

    void query(string sub_string) {
        node* current_node = root;

        for (char ch : sub_string) {
            if (current_node->children.find(ch) == current_node->children.end()) {
                cout << -1 << '\n';
                return;
            }
            current_node = current_node->children[ch];
        }

        if (!current_node->values.empty()) {
            for (int index : current_node->values) {
                cout << index << " ";
            }
            cout << '\n';
        } else {
            cout << -1 << '\n';
        }
    }
};

int main() {
    string s;
    cin >> s;
    s += '$';

    suffix_tree tree;
    tree.construct_tree(s);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string sub_string;
        cin >> sub_string;
        tree.query(sub_string);
    }

    return 0;
}