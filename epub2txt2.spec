%global commit 95ddd43cdde907e7439cd7e85bf32837112770d7
%global shortcommit %(c=%{commit}; echo ${c:0:7}) 
%global gittag v2.0.2

Name:     epub2txt2
Version:  2.0.2
Release:  1%{dist} 
Summary:  Command-line utility for extracting text from EPUB documents
License:  GPL3
URL:      https://github.com/epub2txt2/epub2txt2
 
Source0:  https://github.com/epub2txt2/epub2txt2/archive/%{gittag}/%{name}-%{version}.tar.gz  

BuildRequires: git
BuildRequires: gcc
BuildRequires: make

%define

%description
epub2txt is a simple command-line utility for extracting text from EPUB documents and, optionally, re-flowing it to fit a text display of a particular number of columns. It is written entirely in ANSI-standard C, and should run on any Unix-like system with a C compiler. It is intended for reading EPUB e-books on embedded systems that can't host a graphical EPUB viewer, or converting such e-books to read on those systems. However, it should be robust enough for other purposes, such as batch indexing of EPUB document collections.

%package  epub2txt2 
BuildArch: X86_64 

%prep

%autosetup 

%build
make

%install
make install

%post

%files -f %name.lang
/%_bindir/*
/%_mandir/*

%changelog
* Fri Apr 19 2021 Boyd Kelly <bkelly@coastsystems.net> - 2.0.2
- Initial version of epub2txt2 for Fedora 
