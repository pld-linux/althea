Summary:	An GTK+ IMAP mail client
Summary(pl):	Klient poczty IMAP w GTK+
Name:		althea
Version:	0.5.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0:		%{name}-cxx.patch
Patch1:		%{name}-makefile.patch
URL:		http://althea.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Althea is an SSL aware IMAP mail for X Window System.

%description -l pl
Althea jest klientem poczty IMAP pod X Window System z możliwością
wykorzystania połączeń SSL.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc althearc.example Documentation/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/althea
