# 
# Conditional build:
# _with_ra - use /usr/X11R6 prefix for PLD 1.x
#

Summary:	Kollins - KDE Frontend to YDP Collins' dictionary
Summary(pl):	Kollins - frontend do s³ownika YDP Collinsa dla ¶rodowiska KDE
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
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.1.0
BuildRequires:	libart_lgpl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{?_with_ra:%define	_prefix	/usr/X11R6}
%define		_htmldir	%{_docdir}/kde/HTML

%description
Kollins is KDE Frontend to YDP Collins' dictionary. It supports
English/Polish dictionary as well as German/Polish dictionary.

%description -l pl
Kollins jest frontendem do s³ownika YDP Collinsa dla ¶rodowiska KDE.
Mo¿e korzystaæ zarówno ze s³ownika polsko-angielskiego jak i
polsko-niemieckiego.

%prep
%setup -q
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kollins
%{_applnkdir}/Scientific/*
%{_pixmapsdir}/*/*/*/*.png
