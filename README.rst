=====================
wx_icons_adwaita
=====================

.. start short_desc

**Adwaita icon theme for wxPython 🐍**

.. end short_desc

This package provides a wxPython wxArtProvider class with icons from the Adwaita Icon Theme.

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/custom_wx_icons_adwaita/latest?logo=read-the-docs
	:target: https://custom_wx_icons_adwaita.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/custom_wx_icons_adwaita/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/custom_wx_icons_adwaita/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/custom_wx_icons_adwaita/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/custom_wx_icons_adwaita/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/custom_wx_icons_adwaita/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/custom_wx_icons_adwaita/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/domdfcoding/custom_wx_icons_adwaita/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/custom_wx_icons_adwaita/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/custom_wx_icons_adwaita?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/custom_wx_icons_adwaita
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/wx_icons_adwaita
	:target: https://pypi.org/project/wx_icons_adwaita/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/wx_icons_adwaita?logo=python&logoColor=white
	:target: https://pypi.org/project/wx_icons_adwaita/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/wx_icons_adwaita
	:target: https://pypi.org/project/wx_icons_adwaita/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/wx_icons_adwaita
	:target: https://pypi.org/project/wx_icons_adwaita/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/custom_wx_icons_adwaita
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/custom_wx_icons_adwaita
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/custom_wx_icons_adwaita/v0.2.0
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/custom_wx_icons_adwaita
	:target: https://github.com/domdfcoding/custom_wx_icons_adwaita/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/wx_icons_adwaita
	:target: https://pypi.org/project/wx_icons_adwaita/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/domdfcoding/custom_wx_icons_adwaita/master.svg
	:target: https://results.pre-commit.ci/latest/github/domdfcoding/custom_wx_icons_adwaita/master
	:alt: pre-commit.ci status

.. end shields

Installation
===============

.. start installation

``wx_icons_adwaita`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install wx_icons_adwaita

.. end installation

Usage
============

To use ``wx_icons_adwaita`` in your application:

.. code-block:: python

	from wx_icons_adwaita import wxAdwaitaIconTheme

	class MyApp(wx.App):
		def OnInit(self):
			wx.ArtProvider.Push(wxAdwaitaIconTheme())
			self.frame = TestFrame(None, wx.ID_ANY)
			self.SetTopWindow(self.frame)
			self.frame.Show()
			return True

And then the icons can be accessed through wx.ArtProvider:

.. code-block:: python

	wx.ArtProvider.GetBitmap('document-new', wx.ART_OTHER, wx.Size(48, 48))

Any `FreeDesktop Icon Theme Specification <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_ name can be used.

Currently the `Client ID` is not used, so just pass `wx.ART_OTHER`.
