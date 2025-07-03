const Header = () => {
    return <>
        <div className="header">
            <img src="loogo.svg"/>
            <h1>RandomMedia</h1>
            <div className="navbar">
                <ul>
                    <li>
                        <a>Main Page</a>
                    </li>
                    <li>
                        <a>Current Events</a>
                    </li>
                    <li>
                        <a>Random Article</a>
                    </li>
                </ul>
            </div>
        </div>

    </>
}

export default Header;
