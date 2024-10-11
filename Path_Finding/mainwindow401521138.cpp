#include "QDebug"
#include "QVector"
#include "QWidget"
#include "QString"
#include "QLineEdit"
#include "QTextStream"
#include "mainwindow401521138.h"
#include "ui_mainwindow401521138.h"
MainWindow401521138::MainWindow401521138(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow401521138)
{
    ui->setupUi(this);
    this->setWindowTitle("final_project");
    this->setGeometry(400, 400, 800, 300);
    this->setFixedSize(800, 280);
    this->setStyleSheet("background-color: white;");
    input = new QTextEdit(this);
    output = new QTextEdit(this);
    output->setReadOnly(true);
    gridlayout = new QGridLayout;
    gb = new QGroupBox(this);
    gb->setStyleSheet("background-color: white;");
    btnClear = new QPushButton("CLear", this);
    btnClose = new QPushButton("Close", this);
    btnSubmit = new QPushButton("Submit", this);
    btnReset = new QPushButton("Reset", this);
    Q1 = new QPushButton("Q1", this);
    Q2 = new QPushButton("Q2", this);
    Paste = new QPushButton("Paste TestCase", this);
    btnSubmit->setEnabled(false);
    btnClear->setEnabled(false);
    gridlayout->addWidget(btnClose, 0, 0);
    gridlayout->addWidget(btnReset, 1, 0);
    gridlayout->addWidget(btnClear, 2, 0);
    gridlayout->addWidget(btnSubmit, 3, 0);
    gridlayout->addWidget(Q1, 1, 1);
    gridlayout->addWidget(Q2, 2, 1);
    gb->setLayout(gridlayout);
    gb->setTitle("Group Box");
    gb->move(500, 45);
    gb->resize(200, 200);
    btnReset->setStyleSheet("background-color: #A286EF;color: white;");
    btnSubmit->setStyleSheet("background-color: gray;color: white;");
    btnClear->setStyleSheet("background-color: gray;color: white;");
    btnClose->setStyleSheet("background-color: #A286EF;color: white;");
    Q1->setStyleSheet("background-color: orange;color: white;");
    Q2->setStyleSheet("background-color: orange;color: white;");
    Paste->setStyleSheet("background-color: #ff3399;color: white;");
    Paste->setGeometry(290, 230, 105, 25);
    label1 = new QLabel(this);
    label2 = new QLabel(this);
    label3 = new QLabel(this);
    label1->setText("The least number of train station");
    label2->setText("input:");
    label3->setText("output:");
    label1->setGeometry(220, 50, 205, 20);
    label2->setGeometry(180, 70, 40, 20);
    label3->setGeometry(170, 290, 50, 20);
    label1->setStyleSheet("background-color: white;color: #A286EF;Font: 10pt");
    label2->setStyleSheet("background-color: white;color: #A286EF;Font: 10pt");
    label3->setStyleSheet("background-color: white;color: #A286EF;Font: 10pt");
    input->setGeometry(220, 70, 250, 150);
    input->setStyleSheet("background-color: white;color: blue;");
    output->setGeometry(220, 290, 250, 150);
    output->setFixedSize(250, 150);
    output->setStyleSheet("background-color: white;color: green;");
    output->setVisible(false);
    combotheme = new QComboBox(this);
    combotheme->addItem("Light");
    combotheme->addItem("Dark");
    combotheme->setGeometry(150, 195, 65, 20);
    combotheme->setStyleSheet("background-color: blue;color: white;");
    connect(btnReset, SIGNAL(clicked()), this, SLOT(clear()));
    connect(btnClose, SIGNAL(clicked()), this, SLOT(close()));
    connect(input, SIGNAL(textChanged()), this, SLOT(setEnablebtn()));
    connect(btnSubmit, SIGNAL(clicked()), this, SLOT(submit()));
    connect(Q1, SIGNAL(clicked()), this, SLOT(setText1()));
    connect(Q2, SIGNAL(clicked()), this, SLOT(setText2()));
    connect(btnClear, SIGNAL(clicked()), this, SLOT(clear()));
    connect(btnReset, SIGNAL(clicked()), this, SLOT(clear()));
    connect(Paste, SIGNAL(clicked()), this, SLOT(paste1()));
    connect(combotheme, SIGNAL(currentIndexChanged(int)), this, SLOT(combotheme_changed(int)));
}

MainWindow401521138::~MainWindow401521138() {
    delete ui;
}

void MainWindow401521138::q1() {
    QVector<QString>adj1[1000];

    int n, m, counter;
    QString inputText1 = input->toPlainText();
    QStringList lines1 = inputText1.split('\n');
    QStringList integers1 = lines1[0].split(' ');
    n = integers1[0].toInt();
    m = integers1[1].toInt();

    QString city1, city2, final_city;
    QVector<QString> store1;
    for (int i = 0; i < n; i++) {
         integers1 = lines1[i + 1].split(' ');
         city1 = integers1[0];
         store1.append(city1);
    }

    for (int i = 0; i < m; i++) {
         integers1 = lines1[i + n + 1].split(' ');
         city1 = integers1[0], city2 = integers1[1];
         adj1[find_index(city2, store1)].append(city1);
         adj1[find_index(city1, store1)].append(city2);
    }

    integers1 = lines1[n + m + 1].split(' ');
    final_city = integers1[0];

    QString outText;
    for (int i = 0; i < n; i++) {
         if (store1[i] == final_city)
             outText += store1[i] + " 0\n";
         else {
             bool visited[1000] = {false};
             counter = 0;
             bool flag = false;
             int v = find_index(store1[i], store1);
             visited[v] = true;

             QQueue<int> q;
             q.enqueue(v);

             while(q.size()) {
                 v = q.front();
                 q.dequeue();

                 for (int i = 0; i < adj1[v].size(); i++) {
                      int u = find_index(adj1[v][i], store1);
                      if (!visited[u]) {
                          visited[u] = true;
                          if (adj1[v][i] == final_city) {
                              counter++;
                              flag = true;
                              break;
                          }
                          else
                              q.enqueue(u);
                      }
                  }
                  if (flag)
                      break;
                  else
                      counter++;
             }
             if (flag)
                 outText += store1[i] + QString::number(counter) + "\n";
             else
                 outText += store1[i] + " -1\n";
         }
    }

    output->setPlainText(outText);
}

void MainWindow401521138::q2() {
    int V, E;
    double distance;
    QString city, c, d;
    QString inputText2 = input->toPlainText();
    QStringList lines = inputText2.split('\n');
    QStringList integers2 = lines[0].split(' ');
    V = integers2[0].toInt();
    E = integers2[1].toInt();
    QString Text;

    QVector<QString> store2;
    for (int i = 0; i < V; i++) {
        integers2 = lines[i + 1].split(' ');
        city = integers2[0];
        store2.append(city);
    }

    for (int i = 0; i < E; i++) {
        integers2 = lines[V + i + 1].split(' ');
        distance = integers2[2].toDouble();
        adj[find_index(integers2[0], store2)][find_index(integers2[1], store2)] = 1;
        adj[find_index(integers2[1], store2)][find_index(integers2[0], store2)] = 1;
        w[find_index(integers2[0], store2)][find_index(integers2[1], store2)] = distance;
        w[find_index(integers2[1], store2)][find_index(integers2[0], store2)] = distance;
    }

    integers2 = lines[V + E + 1].split(' ');
    c = integers2[0];
    integers2 = lines[V + E + 2].split(' ');
    d = integers2[0];

    int start = find_index(c, store2);
    int end = find_index(d, store2);
    for (int i = 0; i < V; i++) {
        dist[i] = 100000, visited[i] = false;
    }

    dist[start] = 0;
    QVector<QString> print_shortest_path;
    int parents[400] = {0};
    parents[start] = -1;
    for (int i = 0; i < V - 1; i++) {
        int u = minDiastance(dist, visited, V);
        visited[u] = true;

        for (int x = 0; x < V; x++)
            if (!visited[x] && adj[u][x] && dist[u] != 100000 && dist[u] + w[u][x] < dist[x]) {
                dist[x] = dist[u] + w[u][x];
                parents[x] = u;
            }
    }

    if (dist[end] == 100000)
        Text += "-1\n";
    else {
        Text += QString::number(dist[end], 'f', 2) + "\n";

        int current_vertex = end;
        while (parents[current_vertex] != -1) {
            print_shortest_path.append(store2[parents[current_vertex]]);
            current_vertex = parents[current_vertex];
        }
        for (int i = print_shortest_path.size() - 1; i >= 0; i--)
            Text += print_shortest_path[i] + " ";
        Text += store2[end];
    }

    output->setPlainText(Text);
}

void MainWindow401521138::setEnablebtn() {
    if (input->toPlainText().isEmpty()) {
        btnSubmit->setEnabled(false);
        btnClear->setEnabled(false);
        btnSubmit->setStyleSheet("background-color: gray;color: white;");
        btnClear->setStyleSheet("background-color: gray;color: white;");
    }
    else {
        btnSubmit->setEnabled(true);
        btnClear->setEnabled(true);
        btnSubmit->setStyleSheet("background-color: #A286EF;color: white;");
        btnClear->setStyleSheet("background-color: #A286EF;color: white;");
    }
}

void MainWindow401521138::paste1() {
    if (label1->text() == "The least number of train station") {
        input->setText("4 2\nShiraz\nTehran\nIsfahan\nMashhad\nShiraz Tehran\nMashhad Isfahan\nMashhad");
    }
    else if (label1->text() == "The shortest path to the destination station") {
        input->setText("5 6\nA\nB\nC\nD\nE\nE C 136.81\nD B 12.74\nC B 14.63\nB A 60.48\nA D 45.63\nA E 514.74\nA\nC");
    }
}

void MainWindow401521138::submit() {
    this->setGeometry(400, 400, 800, 600);
    this->setFixedSize(800, 600);
    output->setVisible(true);
    if (label1->text() == "The least number of train station") {
        q1();
    }
    else if (label1->text() == "The shortest path to the destination station")
        q2();
}

void MainWindow401521138::setText1() {
    label1->setText("The least number of train station");
}


void MainWindow401521138::setText2() {
    label1->setText("The shortest path to the destination station");
}

void MainWindow401521138::clear() {
    input->clear();
    output->clear();
    this->setGeometry(400, 400, 800, 300);
    this->setFixedSize(800, 280);
}

void MainWindow401521138::combotheme_changed(int index) {
    if (index == 0) {
        this->setStyleSheet("background-color: white;");
        label1->setStyleSheet("background-color: white;color: #A286EF;Font: 10pt");
        label2->setStyleSheet("background-color: white;color: #A286EF;Font: 10pt");
        label3->setStyleSheet("background-color: white;color: #A286EF;Font: 10pt");
        gb->setStyleSheet("background-color: white;");
    }
    else if (index == 1) {
        this->setStyleSheet("background-color: gray;");
        label1->setStyleSheet("background-color: gray;color: white;Font: 10pt");
        label2->setStyleSheet("background-color: gray;color: white;Font: 10pt");
        label3->setStyleSheet("background-color: gray;color: white;Font: 10pt");
        gb->setStyleSheet("background-color: gray;");
    }
}
