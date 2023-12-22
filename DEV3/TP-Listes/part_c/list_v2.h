#ifndef __LIST__V2_H__
#define __LIST__V2_H__

typedef long long element;
typedef struct list_v2_t *list_v2_p;

extern list_v2_p list_v2_new();
extern void list_v2_insert(list_v2_p list, element value);
extern void list_v2_append(list_v2_p list, element value);

#endif /* !__LIST_H__ */