exp_exec_prefix = /homes/xiao67/apache
exp_bindir = /homes/xiao67/apache/bin
exp_sbindir = /homes/xiao67/apache/bin
exp_libdir = /homes/xiao67/apache/lib
exp_libexecdir = /homes/xiao67/apache/modules
exp_mandir = /homes/xiao67/apache/man
exp_sysconfdir = /homes/xiao67/apache/conf
exp_datadir = /homes/xiao67/apache
exp_installbuilddir = /homes/xiao67/apache/build
exp_errordir = /homes/xiao67/apache/error
exp_iconsdir = /homes/xiao67/apache/icons
exp_htdocsdir = /homes/xiao67/apache/htdocs
exp_manualdir = /homes/xiao67/apache/manual
exp_cgidir = /homes/xiao67/apache/cgi-bin
exp_includedir = /homes/xiao67/apache/include
exp_localstatedir = /homes/xiao67/apache
exp_runtimedir = /homes/xiao67/apache/logs
exp_logfiledir = /homes/xiao67/apache/logs
exp_proxycachedir = /homes/xiao67/apache/proxy
SHLTCFLAGS = -prefer-pic
LTCFLAGS = -prefer-non-pic -static
MKINSTALLDIRS = /homes/xiao67/apache/build/mkdir.sh
INSTALL = $(LIBTOOL) --mode=install /homes/xiao67/apache/build/install.sh -c
MPM_NAME = prefork
INSTALL_DSO = yes
progname = httpd
OS = unix
SHLIBPATH_VAR = LD_LIBRARY_PATH
AP_BUILD_SRCLIB_DIRS = pcre
AP_CLEAN_SRCLIB_DIRS = pcre
bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/bin
cgidir = ${datadir}/cgi-bin
logfiledir = ${localstatedir}/logs
exec_prefix = ${prefix}
datadir = ${prefix}
localstatedir = ${prefix}
mandir = ${prefix}/man
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/modules
htdocsdir = ${datadir}/htdocs
manualdir = ${datadir}/manual
includedir = ${prefix}/include
errordir = ${datadir}/error
iconsdir = ${datadir}/icons
sysconfdir = ${prefix}/conf
installbuilddir = ${datadir}/build
runtimedir = ${localstatedir}/logs
proxycachedir = ${localstatedir}/proxy
other_targets =
progname = httpd
prefix = /homes/xiao67/apache
AWK = gawk
CC = x86_64-pc-linux-gnu-gcc
CPP = x86_64-pc-linux-gnu-gcc -E
CXX =
CPPFLAGS =
CFLAGS =
CXXFLAGS =
LTFLAGS = --silent
LDFLAGS =
LT_LDFLAGS =
SH_LDFLAGS =
LIBS =
DEFS =
INCLUDES =
NOTEST_CPPFLAGS =
NOTEST_CFLAGS =
NOTEST_CXXFLAGS =
NOTEST_LDFLAGS =
NOTEST_LIBS =
EXTRA_CPPFLAGS = -DLINUX -D_REENTRANT -D_GNU_SOURCE
EXTRA_CFLAGS = -pthread
EXTRA_CXXFLAGS =
EXTRA_LDFLAGS = -L/usr/lib64
EXTRA_LIBS = -lm
EXTRA_INCLUDES = -I$(includedir) -I. -I/usr/include/apr-1 -I/usr/include/db4.8
LIBTOOL = /usr/bin/libtool --silent
SHELL = /bin/sh
RSYNC = /usr/bin/rsync
SH_LIBS =
SH_LIBTOOL = $(LIBTOOL)
MK_IMPLIB =
MKDEP = $(CC) -MM
INSTALL_PROG_FLAGS =
APR_BINDIR = /usr/bin
APR_INCLUDEDIR = /usr/include/apr-1
APR_VERSION = 1.4.8
APR_CONFIG = /usr/bin/apr-1-config
APU_BINDIR = /usr/bin
APU_INCLUDEDIR = /usr/include/apr-1
APU_VERSION = 1.5.2
APU_CONFIG = /usr/bin/apu-1-config
