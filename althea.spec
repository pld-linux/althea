Summary:	An GTK+ IMAP mail client
Summary(pl):	Klient poczty IMAP w GTK+
Name:		althea
Version:	0.5.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0:		%{name}-cxx.patch
Patch1:		%{name}-makefile.patch
URL:		http://althea.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Althea is an SSL aware IMAP mail for X Window System.

%description -l pl
Althea jest klinetem poczty IMAP pod X Window System z mo¿liwo¶ci±
wykorzystania po³±czeñ SSL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} CXX=%{__cxx} DEBUGFLAGS="%{rpmcflags}" \
        PIXDIR=%{_datadir}/althea \
        DOCDIR=%{_defaultdocdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	PIXDIR=%{_datadir}/althea

find Documentation -name "CVS" | xargs rm -rf

gzip -9nf althearc.example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Documentation/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/althea
