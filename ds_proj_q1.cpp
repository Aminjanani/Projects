#include <bits/stdc++.h> 
using namespace std;

struct node {
    vector<node*> children;
    char ch;
    vector<int> values;
    node* parent;

    node () {
        parent = nullptr;
    }
};

struct suffix_tree {
    node* root;

    suffix_tree () {
        root->ch = ' ';
    }

    void construct_tree (string s) {
        node* r;
        int size = s.size();
        for (int i = 0; i < size; i++) {
            r = root;
            for (int j = i; j < size; j++) {
                int index = 0;
                bool flag = false;
                if ((int) r->children.size()) {
                    while (true) {
                        if (index == (int) r->children.size()) {
                            break;
                        }
                        else if (r->children[index]->ch == s[j]) {
                            if (j < size - 1) {
                                r = r->children[index];
                            }
                            flag = true;
                            break;
                        } else {
                            index++;
                        }
                    }
                }
                if (!flag) {
                    add_child(s[j], j, r);
                    if (j < size - 1) {
                        r = r->children[index];
                    }
                }
            }
        }
    }

    void add_child (char ch, int index, node* parent) {
        node* new_child;
        new_child->ch = ch;
        new_child->parent = parent;
        if (parent->parent == nullptr) {
            new_child->values.push_back(index);
        }
        parent->children.push_back(new_child);
    }

    void query (string sub_string) {
        bool flag;
        int index = 0;
        node* current_node = root;
        for (int i = 0; i < (int) sub_string.size(); i++) {
            flag = false;
            for (int j = 0; j < (int) current_node->children.size(); j++) {
                if (current_node->children[j]->ch == sub_string[i]) {
                    flag = true;
                    current_node = current_node->children[j];
                    if (current_node->parent == nullptr) {
                        index = j;
                    }
                    break;
                }
            }
            if (!flag) {
                break;
            }
        }
        if (flag) {
            for (int i = 0; i < (int) root->children[index]->values.size(); i++) {
                cout << root->children[index]->values[i] << " ";
            }
        } else {
            cout << -1;
        }
        cout << '\n';
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
