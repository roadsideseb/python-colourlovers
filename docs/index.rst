.. python-colourlovers documentation master file, created by
   sphinx-quickstart on Fri Jan 13 17:41:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-colourlovers's documentation!
===============================================

.. automodule:: colourlovers

ColourLovers
------------

.. autoclass:: colourlovers.ColourLovers

    .. method:: color(argument, **kwargs)

    .. method:: colors(argument=None, **kwargs)
        
        =================== ===================================================
        ``lover``           Restrict results to specific COLOURlover by 
                            providing their user name.
        ``hue_range``       Hue range of the colour: ``12,68``. Values
                            must be in range [0,359] and the left value must be
                            less than the right value.
        ``bri_range``       Brightness range of the colours: ``2,88``. Values
                            must be in range [0, 99] and the left value must
                            be less than the right value.
        ``keywords``	    String of keywords to search for in patterns.
        ``keyword_exact``   Perform an exact search for the keywords passed if 
                            set to 1. Default: 0.
        ``order_col``       ``dateCreated``, ``score``, ``name`, ``numVotes`` 
                            or ``numViews``
        ``sort_by``	    Sorting in asceding (``ASC``) or descending 
                            (``DESC``) order. Defaults to (``ASC``)
        ``num_results``	    Number of results to be returned. Maximum: 100.
                            Default: 20.
        ``result_offset``   Result offset, for paging. Default: 0.
        =================== ===================================================

    .. method:: palette(argument, **kwargs)

    .. method:: palettes(argument=None, **kwargs)

        ======================= ===============================================
        ``lover``               Restrict results to specific COLOURlover by 
                                providing their user name.
        ``hue_option``	        ``yellow``, ``orange``, ``red``  or  ``green``,
                                ``violet``  or ``blue``
        ``hex``	                Restrict results to patterns with a specific
                                colour given as any valid 6-char hex value
                                without preceeding ``#``.
        ``keywords``	        String of keywords to search for in patterns.
        ``keyword_exact``       Perform an exact search for the keywords passed
                                if set to 1. Default: 0.
        ``order_col``           ``dateCreated``, ``score``, ``name`, ``numVotes`` 
                                or ``numViews``
        ``sort_by``	        Sorting in asceding (``ASC``) or descending
                                (``DESC``) order. Defaults to (``ASC``)
        ``num_results``	        Number of results to be returned. Maximum: 100.
                                Default: 20.
        ``result_offset``       Result offset, for paging. Default: 0.
        ``show_palette_widths`` Shows palette's colour's widths if set to 
                                ``1``. Default: ``0``
        ======================= ===============================================

    .. method:: pattern(argument, **kwargs)

    .. method:: patterns(argument=None, **kwargs)

        ==================  ===================================================
        ``lover``           Restrict results to specific COLOURlover by providing
                            their user name.
        ``hue_option``	    ``yellow``, ``orange``, ``red``  or  ``green``,
                            ``violet``  or ``blue``
        ``hex``	            Restrict results to patterns with a specific colour 
                            given as any valid 6-char hex value without 
                            preceeding ``#``.
        ``keywords``	    String of keywords to search for in patterns.
        ``keyword_exact``   Perform an exact search for the keywords passed if 
                            set to 1. Default: 0.
        ``order_col``       ``dateCreated``, ``score``, ``name`, ``numVotes`` 
                            or ``numViews``
        ``sort_by``	    Sorting in asceding (``ASC``) or descending
                            (``DESC``) order. Defaults to (``ASC``)
        ``num_results``	    Number of results to be returned. Maximum: 100.
                            Default: 20.
        ``result_offset``   Result offset, for paging. Default: 0.
        ==================  ===================================================

    .. method:: lover(argument, **kwargs)

        ============    =======================================================
        ``comments``    0 or 1: if 1, will show last 10 comments for given Lover
        ============    =======================================================

    .. method:: lovers(argument=None, **kwargs)

        =================== ===================================================
        ``order_col``       Order in which the colours will be shown. Possible
                            values are: ``dateCreated``, ``score``, ``name`, 
                            ``numVotes`` or ``numViews``.
        ``sort_by``	    Sorting in asceding (``ASC``) or descending 
                            (``DESC``) order. Defaults to (``ASC``)
        ``num_results``	    Number of results to be returned. Maximum: 100.
                            Default: 20.
        ``result_offset``   Result offset, for paging. Default: 0.
        =================== ===================================================

    .. automethod:: colourlovers.ColourLovers.stats(stats_type)

        Request the statistical value (total number) for *stats_type*.
        *stats_type* is a string that can be either of the following: 
        ``colors``, ``patterns``, ``palettes``, ``lovers``.

        Args:
            stats_type (str): Content type to retrieve statistics for.

        Returns:
            Total number of the requested content type on ColourLovers.com.


Colour
------

.. autoclass:: colourlovers.Colour
    :members:


    .. attribute:: id
        
        Unique id for this Color as ``int``.

    .. attribute:: title

        Title / Name of the Color.

    .. attribute:: user_name

       Username of the Color's creator.

    ..  attribute:: num_views

        Number of views this Color has received as ``int``.

    .. attribute:: num_votes

        Number of votes this Color has received as ``int``.

    .. attribute:: num_comments

        Number of comments this Color has received as ``int``.

    ..  attribute:: num_hearts

        Number of hearts this Color has in the range of [0,5] as ``float``.

    .. attribute:: rank
    
        This Color's rank on COLOURlovers.com as ``int``.

    .. attribute:: date_created

        Date this Color was created as a ``datetime`` object.

    .. attribute:: description
        
        This Color's description.

    .. attribute:: url
        
        This Color's COLOURlovers.com URL.

    .. attribute:: image_url

        Link to a PNG version of this Color.

    .. attribute:: badge_url

        Link to a COLOURlovers.com badge for this Color.

    .. attribute:: api_url

        This Color's COLOURlovers.com API URL.

Palette
-------

.. autoclass:: colourlovers.Palette
    :members:

    .. attribute:: id
        
        Unique id for this Palette as ``int``.

    .. attribute:: title
    
        Title / Name of the Palette.

    .. attribute:: user_name
    
        Username of the Palette's creator.

    .. attribute:: num_views
    
        Number of views this Palette has received as ``int``.

    ..  attribute:: num_votes
    
        Number of votes this Palette has received as ``int``.

    .. attribute:: num_comments
    
        Number of comments this Palette has received as ``int``.

    .. attribute:: num_hearts

        Number of hearts this Palette has in the range [0,5] as ``float``.

    .. attribute:: rank
    
        This Palette's rank on COLOURlovers.com as ``int``.

    .. attribute:: date_created
    
        Date this Palette was created as ``datetime`` object.

    .. attribute:: colors
    
        List of Colors within this Palette as hex values

    .. attribute:: color_widths	
    
        This Palette's Color's widths in the range [0.0, 1.0] as ``float``. 

        **Note:** this attribute is optional and might not be present if not
        returned by the API response.

    ..  attribute:: description
    
        This Palette's description

    .. attribute:: url
    
        This Palette's COLOURlovers.com URL.

    .. attribute:: image_url

        Link to a png version of this Palette.

    .. attribute:: badge_url
    
        Link to a COLOURlovers.com badge for this Palette.

    .. attribute:: api_url
    
        This Palette's COLOURlovers.com API URL.

Pattern
-------

.. autoclass:: colourlovers.Pattern
    :members:

    .. attribute:: id
    
        Unique id for this Pattern as ``int``.

    .. attribute:: title
    
        Title / Name of the Pattern.

    .. attribute:: user_name 
    
        Username of the Pattern's creator.

    .. attribute:: num_views
    
        Number of views this Pattern has received as ``int``.

    .. attribute:: num_votes
    
        Number of votes this Pattern has received as ``int``.

    .. attribute:: num_comments
    
        Number of comments this Pattern has received as ``int``.

    .. attribute:: num_hearts
    
        Number of Hearts this Pattern has in the range [0,5] as ``float``.

    .. attribute:: rank
    
        This Pattern's rank on COLOURlovers.com as ``int``.

    .. attribute:: date_created
    
        Date this Pattern was created as ``datetime`` object.

    .. attribute:: colors
    
        List of colors within this Pattern as hex code.

    .. attribute:: description
    
        This Pattern's description.

    .. attribute:: url
            
        This Pattern's COLOURlovers.com URL

    .. attribute:: image_url
        
        Link to a PNG version of this Pattern.

    .. attribute:: badge_url
    
        Link to a COLOURlovers.com badge for this Pattern.

    .. attribute:: api_url
    
        This Pattern's COLOURlovers.com API URL.

Lover
-----

.. autoclass:: colourlovers.Lover
    :members:

    .. attribute:: id
    
        Unique id for this Lover as ``int``.

    .. attribute:: user_name
    
        This Lover's Username.

    .. attribute:: date_registered
    
        Date this Lover registered with COLOURlovers.com as ``datetime`` 
        object.

    .. attribute:: date_last_active
        
        Date this Lover was last active on COLOURlovers.com as ``datetime``
        object.

    .. attribute:: rating

        This Lover's rating

    .. attribute:: location
    
        This Lover's location.

    .. attribute:: num_colors
    
        Number of Colors this Lover has made as ``int``.

    .. attribute:: num_palettes
        
        Number of Palettes this Lover has made as ``int``.

    .. attribute:: num_patterns
    
       Number of Patterns this Lover has made as ``int``.

    .. attribute:: num_comments_made
    
        Number of comments this Lover has made as ``int``.

    .. attribute:: num_lovers
    
        Number of Lovers [friends] this Lover has as ``int``.

    .. attribute:: num_comments_on_profile
    
        Number of comments this Lover has on their profile as ``int``.

    .. attribute:: comments
        
        Last 10 comments made on this Lover's profile as list of
        :py:class:`Comment` instances.

        **Note:** this attribute is optional. It is only returned
        when sending the parameter ``comments=1`` in the request.

    .. attribute:: url
    
        This Lover's COLOURlovers.com URL.

    .. attribute:: api_url
    
        This Lover's COLOURlovers.com API URL.

Stat
----

.. autoclass:: colourlovers.Stat
    :members:

    .. attribute:: total
    
        Total number of colors, palettes, patterns or lovers in the COLOURlovers system.

The RGB and HSV colour classes
------------------------------

.. autoclass:: colourlovers.RGB
    
    .. automethod:: colourlovers.RGB.from_xml

    .. attribute:: red

        Red colour channel in range [0, 255]       

    .. attribute:: green

        Green colour channel in range [0, 255]       

    .. attribute:: blue

        Blue colour channel in range [0, 255]       

    .. autoattribute:: colourlovers.RGB.hex

.. autoclass:: colourlovers.HSV
    
    .. automethod:: colourlovers.HSV.from_xml

    .. attribute:: hue 

        HSV hue channel in range [0, 360]       

    .. attribute:: saturation 

        HSV saturation channel in range [0, 255]       

    .. attribute:: value 

        HSV value channel in range [0, 255]       


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

