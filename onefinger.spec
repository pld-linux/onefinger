# TODO:
# - prepare desktop entry
# - compile python files
Summary:	Graphical interface to the shell
Summary(pl.UTF-8):	Graficzna nakładka na linię poleceń
Name:		onefinger
Version:	4.0
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/onefinger/%{name}_core-%{version}.tar.gz
# Source0-md5:	b47ed00be4ad65dff2383cfef616c575
URL:		http://onefinger.sourceforge.net/
Requires:	python-PyKDE
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Onefinger is a general-purpose GUI (graphical user interface) built on
top of the CLI (command line interface). Although entirely graphical
and "pretty", OneFinger does not attempt to hide the underlying CLI
language: instead, it lets you compose CLI commands with the mouse
(and only one finger!).

%description -l pl.UTF-8
Onefinger jest przeznaczonym do ogólnego użytku GUI (Graficznym
Interfejsem Użytkownika) zbudowanym na podstawie linii poleceń. W
przeciwieństwie do większości graficznych nakładek, OneFinger nie
próbuje ukrywać możliwości linii poleceń, przeciwnie, pozwala wybrać
komendy i przełączniki programów korzystając z myszy(tylko jednym
palcem!).

%prep
%setup -q -n %{name}_core-%{version}

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
%doc AUTHORS CHANGES TODO doc/* web-site/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
