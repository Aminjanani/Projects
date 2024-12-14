#ifndef MAINWINDOW401521138_H
#define MAINWINDOW401521138_H

#include <QMainWindow>
#include <QtWidgets>
#include <QGridLayout>
#include <QGroupBox>
#include <QPushButton>
#include <QVBoxLayout>
#include <QLabel>
#include <QComboBox>
#include <QVector>
#include <QString>
#include <QDebug>
#include <iostream>
#include <string>
#include <QTextStream>
using namespace std;


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow401521138; }
QT_END_NAMESPACE

class MainWindow401521138 : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow401521138(QWidget *parent = nullptr);
    ~MainWindow401521138();
private slots:
    void setEnablebtn();
    void submit();
    void setText1();
    void setText2();
    void clear();
    void paste1();
    void combotheme_changed(int index);
    void q1();
    void q2();
public:
    bool marked[400] = {false};
    bool visited[400];
    bool flag1, flag2;
    int adj[400][400];
    double w[400][400];
    double dist[400];
private:
    Ui::MainWindow401521138 *ui;
    int find_index(QString goal, QVector<QString>store) {
        int index = 0;
            for (int i = 0; i < store.size(); i++) {
                if (store[i] == goal) {
                    index = i;
                    break;
                }
            }
            return index;
    };
    int minDiastance(double dist[], bool visited[], int V) {
        int min = 100000, min_index;;
        for (int i = 0; i < V; i++)
            if (!visited[i] && dist[i] <= min)
                min = dist[i], min_index = i;
        return min_index;
    };
    QLineEdit *input1;
    QLineEdit *input2;
    QTextEdit *input;
    QTextEdit *output;
    QPushButton *btnSubmit;
    QPushButton *btnClear;
    QPushButton *btnReset;
    QPushButton *btnClose;
    QPushButton *Q1;
    QPushButton *Q2;
    QPushButton *Paste;
    QGridLayout *gridlayout;
    QGroupBox *gb;
    QLabel *label1;
    QLabel *label2;
    QLabel *label3;
    QComboBox *combotheme;
};
#endif // MAINWINDOW401521138_H
