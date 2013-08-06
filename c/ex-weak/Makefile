FILE=main.c real.c
OUT=test

.PHONY: all clean
all: $(OUT)

$(OUT): main.o real.o
	$(CC) $(CFLAGS) -o $@ $^

clean:
	-rm $(OUT) *.o
