# This Makefile.am is in the public domain
AM_CPPFLAGS = -I$(top_srcdir)/src/include

if USE_COVERAGE
  AM_CFLAGS = --coverage
endif

lib_LTLIBRARIES = libgnunetfragmentation.la

libgnunetfragmentation_la_SOURCES = \
  fragmentation.c fragmentation.h \
  defragmentation.c
libgnunetfragmentation_la_LIBADD = -lm \
 $(top_builddir)/src/statistics/libgnunetstatistics.la \
 $(top_builddir)/src/util/libgnunetutil.la \
 $(LTLIBINTL)
libgnunetfragmentation_la_LDFLAGS = \
 $(GN_LIB_LDFLAGS) \
  -version-info 2:0:0

check_PROGRAMS = \
 test_fragmentation \
 test_fragmentation_parallel

if ENABLE_TEST_RUN
AM_TESTS_ENVIRONMENT=export GNUNET_PREFIX=$${GNUNET_PREFIX:-@libdir@};export PATH=$${GNUNET_PREFIX:-@prefix@}/bin:$$PATH;unset XDG_DATA_HOME;unset XDG_CONFIG_HOME;
TESTS = $(check_PROGRAMS)
endif

test_fragmentation_SOURCES = \
 test_fragmentation.c
test_fragmentation_LDADD = \
 libgnunetfragmentation.la \
 $(top_builddir)/src/util/libgnunetutil.la

test_fragmentation_parallel_SOURCES = \
 test_fragmentation_parallel.c
test_fragmentation_parallel_LDADD = \
 libgnunetfragmentation.la \
 $(top_builddir)/src/util/libgnunetutil.la

EXTRA_DIST = test_fragmentation_data.conf
