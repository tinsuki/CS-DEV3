#include <stdio.h>
#include <unistd.h>

#include "list_v1.h"
#include "list_v2.h"
#include "time_chrono.h"

void insert_v1()
{
    list_v1_p V1_l11 = list_v1_new();
    
    for (long long i = 0; i < 65536; i++)
    {
        list_v1_insert(V1_l11,i);
    }
}

void insert_v2()
{
    list_v2_p V2_l21 = list_v2_new();
    
    for (long long i = 0; i < 65536; i++)
    {
        list_v2_insert(V2_l21,i);
    }
}

void append_v1()
{
    list_v1_p V1_l12 = list_v1_new();
    
    for (long long i = 0; i < 65536; i++)
    {
        list_v1_append(V1_l12,i);
    }
}

void append_v2()
{
    list_v2_p V2_l22 = list_v2_new();
    
    for (long long i = 0; i < 65536; i++)
    {
        list_v2_append(V2_l22,i);
    }
}

int main()
{
    insert_v1();
    append_v1();
    insert_v2();
    append_v2();

    return 0;
}