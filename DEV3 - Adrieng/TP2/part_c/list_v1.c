#include <stdlib.h>
#include <stdio.h>
#include "list_v1.h"

typedef struct cell_t *cell_p;

typedef struct cell_t
{
    element value;
    cell_p next;
} cell_t;

cell_p cell_new(int value)
{
    cell_p cell = (cell_p) malloc(sizeof(cell_t));
    cell->value = value;
    cell->next = NULL;
    return cell;
}

typedef struct list_v1_t
{
    cell_p first ;
} list_v1_t;

list_v1_p list_v1_new()
{
    list_v1_p list = (list_v1_p) malloc(sizeof(list_v1_t));
    list->first = NULL;
    return list;
}

void list_v1_insert(list_v1_p list, element value)
{
    cell_p new_cell = cell_new(value);

    new_cell->next = list->first;
    list->first = new_cell;
}

void list_v1_append(list_v1_p list, element value)
{
    cell_p new_cell = cell_new(value);

    if(list->first == NULL)
    {
        list->first = new_cell;
    }
    else
    {
        cell_p last_cell = list->first;
        
        while(last_cell->next != NULL)
        {
            last_cell = last_cell->next;
        }

        last_cell->next = new_cell;
    }
}   
