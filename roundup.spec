Summary:	Roundup Issue Tracker
Summary(pl):	Roundup - narzêdzie do ¶ledzenia zg³oszeñ
Name:		roundup
Version:	1.1.1
Release:	0.1
License:	See COPYING.txt
Group:		Applications/WWW
Source0:	http://cheeseshop.python.org/packages/source/r/roundup/%{name}-%{version}.tar.gz
# Source0-md5:	40d74c12c72ff82dbfc8a4f893514dcf
URL:		http://roundup.sourceforge.net/
Requires:	pydoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple-to-use and -install issue-tracking system with command-line,
web and e-mail interfaces. Highly customisable.

%description -l pl
£atwy w u¿yciu i instalacji system ¶ledzenia zg³oszeñ z interfejsami
linii poleceñ, WWW i e-mail. Wysoko konfigurowalny.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,COPYING,README}.txt
