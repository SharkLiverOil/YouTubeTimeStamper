class YouTubeHandler:

    VIDEO_PRE = 'https://youtu.be/'
    TIME_SUFFIX = '?t='

    def __init__(self, link):
        self.link = self._short_link(link)

    def __str__(self):
        return '{}'.format(self.link)

    def _short_link(self, yt_link):
        """
        Takes a YouTube link and makes it a shorter form:
        https://youtu.be/video_id
        :param yt_link: str
        :return: str
        """
        vid_id_idx = yt_link.find('=')
        amp_idx = yt_link.find('&')
        if vid_id_idx != -1 and amp_idx == -1:
            vid_id = yt_link[vid_id_idx+1:]
            return self.VIDEO_PRE + vid_id
        elif amp_idx != -1:
            vid_id = yt_link[vid_id_idx+1:amp_idx]
            return self.VIDEO_PRE + vid_id
        return yt_link