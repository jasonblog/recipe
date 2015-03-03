#
# Makefile
#

ifneq ($(KERNELRELEASE),)
obj-m       += test.o
else

KVERSION := $(shell uname -r)
KERNELDIR ?=/lib/modules/$(KVERSION)/build
PWD := $(shell pwd)
CFLAGS = $(EXTCFLAGS)

all:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

modules_install:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules_install INSTALL_MOD_PATH=$(DIR_TMPFS) INSTALL_MOD_DIR="test"

clean:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) clean

%.i: %.c
	$(MAKE) -C $(KERNELDIR) M=$(PWD) $@

endif
