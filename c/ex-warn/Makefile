
.PHONY: all clean

-include Rule.mk

EXEC :=	ex-warn1

all: $(EXEC)

ex-warn1: ex-warn1.c
	$(CC) $(CFLAGS) -Wall -o $@ $<


clean:
	-rm $(EXEC) 
