import maya.api.OpenMayaAnim as oma
from .ACMEClass  import *
from .clamp      import *
from .frame2time import *
from .time2frame import *
from .linspace   import *


class FrameCtrl(ACMEClass):
    """
    Wrapper class for the maya MAnimControl class

    Attributes
    ----------
    begin : int
        the starting frame number
    end : int
        the ending frame number
    current : int
        the current frame number

    Methods
    -------
    length()
        returns the animation length in frames
    reset()
        sets the current frame to begin
    step(n)
        shifts the current frame by n
    next()
        advances to the next frame
    prev()
        set back to the previous frame
    sample(n)
        evenly samples the animation frame range [begin, end] in n parts
    to_range()
        converts the animation frame range [begin, end] into a range
    to_list()
        converts the animation frame range [begin, end] into a list
    """

    def __init__(self):
        super(self, ACMEClass).__init__()

    def length(self):
        """
        Returns the animation length in frames

        Returns
        -------
        int
            the animation length
        """

        return self.end - self.begin

    @property
    def begin(self):
        """
        Returns the begin frame number

        Returns
        -------
        int
        """

        return time2frame(oma.MAnimControl.animationStartTime())

    @begin.setter
    def begin(self, frame):
        """
        Sets the beginning frame number

        Parameters
        ----------
        frame : int
            the frame number

        Returns
        -------
        None
        """

        oma.MAnimControl.setAnimationStartTime(frame2time(frame))

    @property
    def end(self):
        """
        Returns the end frame number

        Returns
        -------
        int
        """

        return time2frame(oma.MAnimControl.animationEndTime())

    @end.setter
    def end(self, frame):
        """
        Sets the ending frame number

        Parameters
        ----------
        frame : int
            the frame number

        Returns
        -------
        None
        """

        oma.MAnimControl.setAnimationEndTime(frame2time(frame))

    @property
    def current(self):
        """
        Returns the current frame number

        Returns
        -------
        int
        """

        return time2frame(oma.MAnimControl.getCurrentTime())

    @current.setter
    def current(self, frame):
        """
        Sets the current frame number

        Parameters
        ----------
        frame : int
            the frame number

        Returns
        -------
        None
        """

        oma.MAnimControl.setCurrentTime(frame2time(clamp(frame, self.begin, self.end)))

    def reset(self):
        """
        Sets the current frame to begin

        Returns
        -------
        None
        """

        self.current = self.begin

    def step(self, n):
        """
        Shifts the current frame by n

        Parameters
        ----------
        n : int
            the number of frame to skip

        Returns
        -------
        None
        """

        self.current += n

    def next(self):
        """
        Advances to the next frame

        Returns
        -------
        None
        """

        self.step(1)

    def prev(self):
        """
        Set back to the previous frame

        Returns
        -------
        None
        """

        self.step(-1)

    def sample(self, n):
        """
        Evenly samples the animation frame range [begin, end] in n parts

        Parameters
        ----------
        n : int
            the number of samples

        Returns
        -------
        list
            the sampled frame numbers
        """

        return linspace(self.begin, self.end, n, dtype=int)

    def to_range(self):
        """
        Converts the animation frame range [begin, end] into a range

        Returns
        -------
        range
            the [begin, end] range
        """

        return range(self.begin, self.end+1)

    def to_list(self):
        """
        Converts the animation frame range [begin, end] into a list

        Returns
        -------
        list
            the [begin, end] list
        """

        return list(self.to_range())

    def is_begin(self):
        """
        Returns True if the current frame is the starting frame

        Returns
        -------
        bool
            True if the current frame is the starting frame
        """

        return self.current == self.begin

    def is_end(self):
        """
        Returns True if the current frame is the ending frame

        Returns
        -------
        bool
            True if the current frame is the ending frame
        """

        return self.current == self.end

    def extra_repr(self):
        return '[{}, {}], current={}'.format(self.begin, self.end, self.current)
