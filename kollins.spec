# 
# Conditional build:
# _with_ra - use /usr/X11R6 prefix for PLD 1.x
#

Summary:	Kollins - KDE Frontend to YDP Collins' dictionary
Summary(pl):	Kollins - frontend s³ownka YDP Collins dla ¶rodowiska KDE
Name:		kollins
Version:	0.2
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	009d3b3a1a99b5b29670011c5d69bd55
Patch0:		%{name}-desktopdir_location.patch
URL:		http://sourceforge.net/projects/kollins/
BuildRequires:	kdelibs-devel >= 3.1.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	fam-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{?_with_ra:%define	_prefix	/usr/X11R6}

%description
Kollins is KDE Frontend to YDP Collins' dictionary. It supports
English/Polish dictionary as well as German/Polish dictionary.

%description -l pl
Kollins jest frontendem s³ownika YDP Collins dla ¶rodowiska KDE. Mo¿e
korzystaæ zarówno ze s³ownkika polsko-angielskiego jak
polsko-niemieckiego.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if 0%{!?_with_ra:1}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Scientific/* \
	$RPM_BUILD_ROOT%{_applnkdir}/Scientific/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/doc/HTML/en/kollins
%{_datadir}/locale/pl/LC_MESSAGES/kollins.mo
%{_datadir}/icons/hicolor/32x32/actions/*
%{_datadir}/icons/hicolor/16x16/*
%{_datadir}/apps/kollins
%{_applnkdir}/Scientific/*
%{_datadir}/icons/hicolor/32x32/apps/*
