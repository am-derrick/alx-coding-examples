#ifndef _CAR_H_
#define _CAR_H_

/**
 * struct car - info about my cool car
 * @name: name of the car
 * @class: class of the car
 * @number: number of the car
 */
struct car
{
	char *name;
	char *class;
	int number;
};

/**
 * car_t - Typedef for struct car
 */
typedef struct car car_t;

#endif /* _CAR_H_ */
