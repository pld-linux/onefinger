Summary:	Graphical interface to the shell
Summary(pl):	Graficzna nak�adka na lini� polece�
Name:		onefinger
Version:	1.1.1
Release:	1
Url:		http://onefinger.sourceforge.net/
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	1d05f2c688f9abe3a1771b2c0f0f5bb8
BuildArch:	noarch
BuildRequires:	ImageMagick
Requires:	python-PyQt
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Onefinger is a general-purpose GUI (graphical user interface) built on
top of the CLI (command line interface). Although entirely graphical
and "pretty", OneFinger does not attempt to hide the underlying CLI
language: instead, it lets you compose CLI commands with the mouse
(and only one finger!).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir}}
cp -r src/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cat <<EOF >$RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/%{name}/python
python one-finger.py $*
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README TODO doc/* web-site/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
