#
#   Copyright (c) 2015, Scott J Maddox
#
#   This file is part of Open Band Parameters Device Simulator (OBPDS).
#
#   OBPDS is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   OBPDS is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with OBPDS.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################


__all__ = ['Contact', 'OhmicContact', 'SchottkyContact']


class Contact(object):
    pass

class OhmicContact(Contact):
    pass

class SchottkyContact(Contact):
    '''
    A Schottky contact that pins at the "universal pinning level",
    which is approximately 4.9 eV below the vacuum level.
    '''
    def __init__(self, work_function=4.9):
        self.work_function = work_function