# Copyright (c) 2013 The F9 Microkernel Project. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

CONFIG := .config

ifneq (,$(wildcard $(CONFIG)))
include $(CONFIG)
else
all: config_error
.PHONY: config_error
config_error:
	@echo "Please ensure that it is configured by 'make config'"
	@$(MAKE) -s UNKNOWN 2>/dev/null
endif

BOARD ?= skeleton

# output directory for build objects
out ?= build/$(BOARD)

# output directory for host build boardss
out_host ?= build/host

# toolchain specific configurations; common cflags and ldflags
include mk/toolchain.mk

# obtain CHIP name
include boards/$(BOARD)/build.mk

# Transform the configuration into make variables
includes = \
	boards/$(BOARD) \
	include \
	$(dirs) $(out)
$(eval CONFIG_BOARD_$(BOARD)=y)

# Get build configuration from sub-directories
include user/build.mk

includes += $(includes-y)

objs_from_dir = $(foreach obj, $($(2)-y), \
		$(out)/$(1)/$(firstword $($(2)-mock-$(PROJECT)-$(obj)) $(obj)))

# Get all sources to build
all-y += $(call objs_from_dir,platform/$(CHIP),chip)
all-y += $(call objs_from_dir,boards/$(BOARD),boards)
all-y += $(call objs_from_dir,platform,platform)
all-y += $(call objs_from_dir,kernel/lib,kernel-lib)
all-y += $(call objs_from_dir,kernel,kernel)
all-y += $(call objs_from_dir,user,user)
dirs = \
	kernel/lib \
	kernel \
	platform/$(CHIP) \
	boards/$(BOARD) \
	user

# Get special rules
dir-rules := mk/rules
$(foreach rule, $(shell ls $(dir-rules)), \
	$(eval include $(dir-rules)/$(rule)))

include mk/generic.mk
