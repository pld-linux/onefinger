# TODO:
# - prepare desktop entry
# - compile python files
Summary:	Graphical interface to the shell
Summary(pl):	Graficzna nak³adka na liniê poleceñ
Name:		onefinger
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/onefinger/%{name}-%{version}.tar.gz
# Source0-md5:	1d05f2c688f9abe3a1771b2c0f0f5bb8
URL:		http://onefinger.sourceforge.net/
Requires:	python-PyQt
BuildArch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Onefinger is a general-purpose GUI (graphical user interface) built on
top of the CLI (command line interface). Although entirely graphical
and "pretty", OneFinger does not attempt to hide the underlying CLI
language: instead, it lets you compose CLI commands with the mouse
(and only one finger!).

%description -l pl
Onefinger jest przeznaczonym do ogólnego u¿ytku GUI (Graficznym
Interfejsem U¿ytkownika) zbudowanym na podstawie linii poleceñ. W
przeciwieñstwie do wiêkszo¶ci graficznych nak³adek, OneFinger nie
próbuje ukrywaæ mo¿liwo¶ci linii poleceñ, przeciwnie, pozwala wybraæ
komendy i prze³±czniki programów korzystaj±c z myszy(tylko jednym
palcem!).

%prep
%setup -q

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
%doc AUTHORS CHANGES README TODO doc/* web-site/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
