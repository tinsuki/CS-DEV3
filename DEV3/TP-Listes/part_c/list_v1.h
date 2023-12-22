#ifndef __LIST__V1_H__
#define __LIST__V1_H__

typedef long long element;
typedef struct list_v1_t *list_v1_p;

extern list_v1_p list_v1_new();
extern void list_v1_insert(list_v1_p list, element value);
extern void list_v1_append(list_v1_p list, element value);

#endif /* !__LIST_H__ */