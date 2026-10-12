-- Render inline code as breakable \path{} in LaTeX (long registered identifiers).
-- Inside captions (moving arguments) use a robust \texttt{} with escaped characters instead.
local function tt(text)
  local s = text:gsub('\\', '\\textbackslash{}'):gsub('([_%%#&{}$])', '\\%1')
  return pandoc.RawInline('latex', '\\texttt{' .. s .. '}')
end
local caption_pass = {
  Table = function(t)
    t.caption = pandoc.walk_block(pandoc.Div(t.caption.long), {Code = function(c) return tt(c.text) end}).content and
      {long = pandoc.walk_block(pandoc.Div(t.caption.long), {Code = function(c) return tt(c.text) end}).content, short = t.caption.short} or t.caption
    return t
  end,
  Figure = function(f)
    f.caption.long = pandoc.walk_block(pandoc.Div(f.caption.long), {Code = function(c) return tt(c.text) end}).content
    return f
  end,
}
local code_pass = {
  Code = function(el)
    if FORMAT:match('latex') and el.text:find(' ') then
      return tt(el.text)
    elseif FORMAT:match('latex') and not el.text:find('[{}%%#\\]') then
      return pandoc.RawInline('latex', '\\path{' .. el.text .. '}')
    end
  end,
}
return {caption_pass, code_pass}
