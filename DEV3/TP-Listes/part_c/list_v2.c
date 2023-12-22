#include <stdlib.h>
#include <stdio.h>
#include "list_v2.h"

typedef struct list_v2_t
{
    element *array;
    size_t array_size;
    size_t number_of_elements;
} list_v2_t;

list_v2_p list_v2_new()
{
    list_v2_p list = (list_v2_p) malloc(sizeof(list_v2_t));
    list->array = (element *) malloc(sizeof(element));
    list->array_size = 1;
    list->number_of_elements = 0;
    return list;
}

void list_v2_insert(list_v2_p list, element value)
{
    if(list->number_of_elements == list->array_size)
    {
        list->array = (element *) realloc(list->array, 2*list->array_size * sizeof(element));
        list->array_size *= 2;
    }

    for(int i = list->number_of_elements ; i > 0 ; i-- )
    {
            list->array[i] = list->array[i-1];
    }
    list->array[0] = value;
    list->number_of_elements++;
}

void list_v2_append(list_v2_p list, element value)
{
    if(list->number_of_elements == list->array_size)
    {
        list->array = (element *) realloc(list->array, 2*list->array_size * sizeof(element));
        list->array_size *= 2;
    }
    list->array[list->number_of_elements] = value;
    list->number_of_elements++;
}   
