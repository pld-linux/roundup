Summary:	Roundup Issue Tracker
Summary(pl.UTF-8):	Roundup - narzędzie do śledzenia zgłoszeń
Name:		roundup
Version:	1.4.6
Release:	0.1
License:	distributable (BSD-like, see COPYING.txt)
Group:		Applications/WWW
Source0:	http://cheeseshop.python.org/packages/source/r/roundup/%{name}-%{version}.tar.gz
# Source0-md5:	e364bb8026761829752ffec76e33065f
URL:		http://roundup.sourceforge.net/
Patch0:		%{name}-mandir.patch
BuildRequires:	rpm-pythonprov
Requires:	pydoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple-to-use and -install issue-tracking system with command-line,
web and e-mail interfaces. Highly customisable.

%description -l pl.UTF-8
Łatwy w użyciu i instalacji system śledzenia zgłoszeń z interfejsami
linii poleceń, WWW i e-mail. Wysoko konfigurowalny.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {CHANGES,COPYING,README}.txt doc/*txt
%attr(755,root,root) %{_bindir}/roundup-*
%{py_sitescriptdir}/roundup
%{_datadir}/roundup
%{_mandir}/man1/*
